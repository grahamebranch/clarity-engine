// --- TAB LOGIC ---
document.querySelectorAll("#tabs button").forEach(btn => {
    btn.addEventListener("click", () => {
        const target = btn.dataset.target;

        document.querySelectorAll("section").forEach(sec => {
            if (sec.id.endsWith("-panel") && sec.id !== "input-panel" && sec.id !== "output-panel") {
                sec.classList.add("hidden");
            }
        });

        document.getElementById(target).classList.remove("hidden");
    });
});


// --- EVENT SENDER (analytics pipe) ---
async function sendEvent(type, metadata = {}) {
    const sessionId = getSessionId();

    await fetch("/analytics", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            sessionId,
            type,
            metadata,
            timestamp: Date.now()
        })
    });
}


// --- SESSION ID ---
function getSessionId() {
    let id = sessionStorage.getItem("clarity_session_id");
    if (!id) {
        id = crypto.randomUUID();
        sessionStorage.setItem("clarity_session_id", id);
    }
    return id;
}


// --- METADATA HELPERS ---
function detectDocumentType(text) {
    if (text.includes("@") && text.includes("Subject")) return "email";
    if (text.length > 800) return "long_form";
    if (text.split("\n").length > 5) return "multi_paragraph";
    return "short_note";
}

function detectPromptIntent(text) {
    const t = text.toLowerCase();
    if (t.startsWith("rewrite")) return "rewrite";
    if (t.startsWith("summarise") || t.startsWith("summarize")) return "summary";
    if (t.startsWith("explain")) return "explain";
    return "unknown";
}

function detectLanguage(text) {
    return navigator.language || "unknown";
}

function complexityScore(text) {
    const words = text.split(/\s+/).length;
    if (words < 50) return "simple";
    if (words < 200) return "medium";
    return "complex";
}


// --- RUN ENGINE (WIRED TO BACKEND) ---
document.getElementById("run-btn").addEventListener("click", async () => {
    const text = document.getElementById("input-text").value;

    // Analytics: engine run
    sendEvent("engine_run", {
        inputLength: text.length
    });

    // Send to backend
    const response = await fetch("/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text })
    });

    const data = await response.json();

    // Fill panels
    document.getElementById("output-text").textContent = data.output || "";
    document.getElementById("sections-content").textContent = JSON.stringify(data.sections, null, 2);
    document.getElementById("trace-content").textContent = JSON.stringify(data.trace, null, 2);
    document.getElementById("quality-content").textContent = JSON.stringify(data.quality, null, 2);

    // Analytics: metadata
    sendEvent("metadata", {
        docType: detectDocumentType(text),
        intent: detectPromptIntent(text),
        language: detectLanguage(text),
        complexity: complexityScore(text)
    });
});


// --- DROP-OFF TRACKING ---
window.addEventListener("beforeunload", () => {
    sendEvent("session_end");
});

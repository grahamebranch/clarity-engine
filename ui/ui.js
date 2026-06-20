// ui.js — FastPath Whole-File Replacement
// Clarity Companion — UI/Engine Integration Stabilisation

document.addEventListener("DOMContentLoaded", () => {
    const generateBtn = document.getElementById("generateBtn");
    const clearBtn = document.getElementById("clearBtn");
    const topicInput = document.getElementById("topicInput");
    const outputContainer = document.getElementById("outputContainer");
    const statusBar = document.getElementById("statusBar");
    const metadataBar = document.getElementById("metadataBar");

    // -----------------------------
    // STATE
    // -----------------------------
    let isLoading = false;

    // -----------------------------
    // UI HELPERS
    // -----------------------------
    function setLoading(state) {
        isLoading = state;

        if (state) {
            statusBar.innerText = "Generating lesson…";
            statusBar.className = "status loading";
            generateBtn.disabled = true;
            outputContainer.classList.add("adaptive-soft");
        } else {
            statusBar.innerText = "";
            statusBar.className = "status";
            generateBtn.disabled = false;
            outputContainer.classList.remove("adaptive-soft");
        }
    }

    function showError(msg) {
        statusBar.innerText = msg;
        statusBar.className = "status error";
        outputContainer.classList.add("adaptive-error");
    }

    function clearUI() {
        topicInput.value = "";
        outputContainer.innerHTML = "";
        metadataBar.innerHTML = "";
        statusBar.innerText = "";
        statusBar.className = "status";
        outputContainer.className = "";
    }

    function applyAdaptiveLayout(lesson) {
        const sectionCount = lesson.sections.length;

        if (sectionCount <= 3) {
            outputContainer.classList.add("adaptive-compact");
        } else {
            outputContainer.classList.add("adaptive-expanded");
        }

        if (lesson.tone === "reflective") {
            outputContainer.classList.add("adaptive-soft");
        } else if (lesson.tone === "technical") {
            outputContainer.classList.add("adaptive-sharp");
        }
    }

    // -----------------------------
    // RENDERING
    // -----------------------------
    function renderLesson(lesson) {
        outputContainer.innerHTML = "";

        lesson.sections.forEach(sec => {
            const div = document.createElement("div");
            div.className = "lesson-section";

            div.innerHTML = `
                <h3>${sec.title}</h3>
                <p>${sec.content}</p>
            `;

            outputContainer.appendChild(div);
        });

        metadataBar.innerHTML = `
            <div class="meta-item">Engine v${lesson.engine_version}</div>
            <div class="meta-item">Domain Pack: ${lesson.domain}</div>
            <div class="meta-item">Generated: ${new Date().toLocaleString()}</div>
        `;

        applyAdaptiveLayout(lesson);
    }

    // -----------------------------
    // ENGINE CALL
    // -----------------------------
    async function generateLesson() {
        const topic = topicInput.value.trim();
        if (!topic) {
            showError("Please enter a topic.");
            return;
        }

        clearUI();
        setLoading(true);

        try {
            const response = await fetch("/generate_lesson", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ topic })
            });

            if (!response.ok) {
                throw new Error("Engine returned an error.");
            }

            const data = await response.json();

            if (!data || !data.sections) {
                throw new Error("Malformed engine response.");
            }

            renderLesson(data);
        } catch (err) {
            showError("Error: " + err.message);
        } finally {
            setLoading(false);
        }
    }

    // -----------------------------
    // EVENT LISTENERS
    // -----------------------------
    generateBtn.addEventListener("click", generateLesson);
    clearBtn.addEventListener("click", clearUI);
});

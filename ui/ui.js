// ------------------------------------------------------------
// Clarity Engine UI — FastPath Version
// Full drop‑in replacement for ui.js
// ------------------------------------------------------------

// Elements
const inputEl = document.getElementById("inputText");
const runBtn = document.getElementById("runButton");

const outText = document.getElementById("improvedText");
const outSections = document.getElementById("sections");
const outTrace = document.getElementById("trace");
const outQuality = document.getElementById("quality");
const outDiagnostics = document.getElementById("diagnostics-output");

// ------------------------------------------------------------
// Render helpers
// ------------------------------------------------------------

function renderOutput(text) {
    outText.textContent = text || "";
}

function renderSections(sections) {
    outSections.textContent = JSON.stringify(sections, null, 2);
}

function renderTrace(trace) {
    outTrace.textContent = JSON.stringify(trace, null, 2);
}

function renderQuality(quality) {
    outQuality.textContent = JSON.stringify(quality, null, 2);
}

function renderDiagnostics(diag) {
    outDiagnostics.textContent = JSON.stringify(diag, null, 2);
}

// ------------------------------------------------------------
// Engine call
// ------------------------------------------------------------

async function runEngine() {
    const userText = inputEl.value || "";

    // POST to your engine endpoint (corrected: /run)
    const response = await fetch("https://zany-computing-machine-gx47prv67g97fwpgv-8000.app.github.dev/run", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: userText })
    });

    const result = await response.json();

    // Render everything
    renderOutput(result.text);
    renderSections(result.sections);
    renderTrace(result.trace);
    renderQuality(result.quality);
    renderDiagnostics(result.diagnostics);
}

// ------------------------------------------------------------
// Bind
// ------------------------------------------------------------

runBtn.addEventListener("click", () => {
    runEngine().catch(err => {
        outText.textContent = "Engine error: " + err;
    });
});

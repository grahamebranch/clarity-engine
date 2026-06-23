const inputBox = document.getElementById("inputBox");
const runButton = document.getElementById("runButton");
const outputBox = document.getElementById("outputBox");
const errorBox = document.getElementById("errorBox");
const clarityScoreEl = document.getElementById("clarityScore");
const outputLengthEl = document.getElementById("outputLength");
const timestampEl = document.getElementById("timestamp");
const sectionsBox = document.getElementById("sectionsBox");
const darkModeToggle = document.getElementById("darkModeToggle");
const panelToggles = document.querySelectorAll(".panel-toggle");

let streamingInterval = null;

// ---------------------------------------------------------
// API CALL
// ---------------------------------------------------------
async function callEngine(text) {
  const response = await fetch(
    "https://zany-computing-machine-gx47prv67g97fwpgv-8000.app.github.dev/generate",
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text })
    }
  );

  if (!response.ok) {
    throw new Error("Engine request failed");
  }

  return await response.json();
}

// ---------------------------------------------------------
// SIMULATED STREAMING
// ---------------------------------------------------------
function simulateStreaming(fullText) {
  if (streamingInterval) {
    clearInterval(streamingInterval);
    streamingInterval = null;
  }

  outputBox.textContent = "";
  let index = 0;
  const chunkSize = 4; // characters per tick
  const delay = 20; // ms per tick

  streamingInterval = setInterval(() => {
    if (index >= fullText.length) {
      clearInterval(streamingInterval);
      streamingInterval = null;
      return;
    }
    const nextChunk = fullText.slice(index, index + chunkSize);
    outputBox.textContent += nextChunk;
    index += chunkSize;
  }, delay);
}

// ---------------------------------------------------------
// RENDER METADATA
// ---------------------------------------------------------
function renderMetadata(result) {
  clarityScoreEl.textContent = result.clarity_score;
  outputLengthEl.textContent = result.output.length;
  timestampEl.textContent = new Date().toISOString();

  sectionsBox.innerHTML = "";
  if (result.sections && result.sections.length > 0) {
    result.sections.forEach((section) => {
      const div = document.createElement("div");
      div.className = "section-item";

      const title = document.createElement("div");
      title.className = "section-title";
      title.textContent = section.title;

      const content = document.createElement("div");
      content.className = "section-content";
      content.textContent = section.content;

      div.appendChild(title);
      div.appendChild(content);
      sectionsBox.appendChild(div);
    });
  } else {
    const empty = document.createElement("div");
    empty.className = "section-item";
    empty.textContent = "No sections detected.";
    sectionsBox.appendChild(empty);
  }
}

// ---------------------------------------------------------
// MAIN HANDLER
// ---------------------------------------------------------
async function runEngine() {
  const text = inputBox.value.trim();
  if (!text) return;

  errorBox.innerText = "";
  outputBox.textContent = "Processing…";
  clarityScoreEl.textContent = "–";
  outputLengthEl.textContent = "–";
  timestampEl.textContent = "–";
  sectionsBox.innerHTML = "";
  runButton.disabled = true;

  try {
    const result = await callEngine(text);
    simulateStreaming(result.output);
    renderMetadata(result);
  } catch (err) {
    console.error(err);
    errorBox.innerText = "Engine failed to process text.";
    outputBox.textContent = "";
  } finally {
    runButton.disabled = false;
  }
}

// ---------------------------------------------------------
// DARK MODE
// ---------------------------------------------------------
darkModeToggle.addEventListener("click", () => {
  document.body.classList.toggle("dark-mode");
});

// ---------------------------------------------------------
// PANEL COLLAPSE
// ---------------------------------------------------------
panelToggles.forEach((btn) => {
  btn.addEventListener("click", () => {
    const target = btn.getAttribute("data-target");
    const panel = document.querySelector(`.panel[data-panel="${target}"]`);
    if (!panel) return;

    const collapsed = panel.classList.toggle("collapsed");
    btn.textContent = collapsed ? "+" : "−";
  });
});

// ---------------------------------------------------------
// KEYBOARD SHORTCUTS
// ---------------------------------------------------------
document.addEventListener("keydown", (e) => {
  // Ctrl+Enter => run
  if (e.key === "Enter" && (e.ctrlKey || e.metaKey)) {
    e.preventDefault();
    runEngine();
    return;
  }

  // D => dark mode
  if (e.key === "d" || e.key === "D") {
    document.body.classList.toggle("dark-mode");
    return;
  }

  // M => toggle metadata panel
  if (e.key === "m" || e.key === "M") {
    const panel = document.querySelector('.panel[data-panel="metadata"]');
    const btn = document.querySelector('.panel-toggle[data-target="metadata"]');
    if (panel && btn) {
      const collapsed = panel.classList.toggle("collapsed");
      btn.textContent = collapsed ? "+" : "−";
    }
  }
});

// ---------------------------------------------------------
// BUTTON WIRING
// ---------------------------------------------------------
runButton.addEventListener("click", runEngine);

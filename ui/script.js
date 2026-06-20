console.log("SCRIPT VERSION 100");

// ---------------------------------------------------------
// CLARITY ENGINE (existing)
// ---------------------------------------------------------

document.getElementById("runButton").addEventListener("click", async () => {
    const inputText = document.getElementById("inputText").value;

    try {
        const response = await fetch("https://zany-computing-machine-gx47prv67g97fwpgv-8000.app.github.dev/run_engine", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: inputText })
        });

        const data = await response.json();

        document.getElementById("improvedText").textContent = data.text;
        document.getElementById("sections").textContent = JSON.stringify(data.sections, null, 2);
        document.getElementById("trace").textContent = JSON.stringify(data.trace, null, 2);
        document.getElementById("quality").textContent = JSON.stringify(data.quality, null, 2);

    } catch (error) {
        console.error("Error calling backend:", error);
        document.getElementById("improvedText").textContent = "Error contacting backend.";
    }
});


// ---------------------------------------------------------
// LESSON ENGINE (new)
// ---------------------------------------------------------

document.getElementById("lessonButton").addEventListener("click", async () => {
    const topic = document.getElementById("lessonTopic").value;
    const level = document.getElementById("lessonLevel").value;
    const domain = document.getElementById("lessonDomain").value;
    const edition = document.getElementById("lessonEdition").value;

    // Packs: comma-separated → array
    const packsRaw = document.getElementById("lessonPacks").value;
    const packs = packsRaw
        .split(",")
        .map(p => p.trim())
        .filter(p => p.length > 0);

    try {
        const response = await fetch("https://zany-computing-machine-gx47prv67g97fwpgv-8000.app.github.dev/lesson", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                topic,
                level,
                domain,
                edition,
                packs
            })
        });

        const data = await response.json();

        // Render metadata
        document.getElementById("lessonMetadata").textContent =
            JSON.stringify(data.metadata, null, 2);

        // Render sections
        document.getElementById("lessonSections").textContent =
            JSON.stringify(data.sections, null, 2);

        // Render annexes
        document.getElementById("lessonAnnexes").textContent =
            JSON.stringify(data.annexes, null, 2);

    } catch (error) {
        console.error("Error calling lesson backend:", error);
        document.getElementById("lessonMetadata").textContent = "Error contacting backend.";
    }
});

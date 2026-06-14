document.getElementById("runButton").addEventListener("click", async () => {
    const inputText = document.getElementById("inputText").value;

    const response = await fetch("https://zany-computing-machine-gx47prv67g97fwpgv-8000.app.github.dev/clarity", {

        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: inputText })
    });

    const data = await response.json();

    document.getElementById("improvedText").textContent = data.improved_text;
    document.getElementById("sections").textContent = JSON.stringify(data.sections, null, 2);
    document.getElementById("trace").textContent = JSON.stringify(data.trace, null, 2);
    document.getElementById("quality").textContent = JSON.stringify(data.quality, null, 2);
});

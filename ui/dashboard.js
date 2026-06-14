async function loadAnalytics() {
    const res = await fetch("/analytics-log");
    const lines = (await res.text()).trim().split("\n");
    return lines.map(l => JSON.parse(l));
}

function countBy(events, key) {
    const out = {};
    events.forEach(e => {
        const val = e.metadata?.[key];
        if (!val) return;
        out[val] = (out[val] || 0) + 1;
    });
    return out;
}

function render(id, data) {
    const el = document.getElementById(id);
    el.innerHTML = Object.entries(data)
        .map(([k, v]) => `${k}: ${v}`)
        .join("<br>");
}

async function main() {
    const events = await loadAnalytics();

    const sessions = events.filter(e => e.type === "session_start");
    const runs = events.filter(e => e.type === "engine_run");
    const metadata = events.filter(e => e.type === "metadata");

    render("sessions-per-day", { sessions: sessions.length });
    render("runs-per-day", { runs: runs.length });

    render("doc-types", countBy(metadata, "docType"));
    render("prompt-intents", countBy(metadata, "intent"));
    render("languages", countBy(metadata, "language"));
    render("devices", countBy(runs, "device"));
    render("countries", countBy(runs, "country"));

    // Session length (rough)
    const endEvents = events.filter(e => e.type === "session_end");
    render("session-length", { ends: endEvents.length });
}

main();

"""
EL12 - Deterministic Trace Layer (v1.0)

Purpose:
- Record what each layer did without modifying the text
- Provide before/after snapshots for debugging and introspection
- Deterministic, no rewriting, no semantic changes
"""

from dataclasses import dataclass, asdict


@dataclass
class TraceEntry:
    layer: str
    before: str
    after: str
    changed: bool


class EL12Trace:
    def __init__(self):
        self._trace_log = []

    def record(self, layer_name: str, before: str, after: str):
        entry = TraceEntry(
            layer=layer_name,
            before=before,
            after=after,
            changed=(before != after),
        )
        self._trace_log.append(asdict(entry))

    def get_trace(self):
        return self._trace_log

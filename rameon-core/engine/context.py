from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class EngineContext:
    """
    Holds configuration, runtime state, and shared resources for the engine.
    Passed through the engine lifecycle.
    """

    config: Dict[str, Any] = field(default_factory=dict)
    state: Dict[str, Any] = field(default_factory=dict)

    def set(self, key: str, value: Any) -> None:
        """Store a value in the runtime state."""
        self.state[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a value from the runtime state."""
        return self.state.get(key, default)

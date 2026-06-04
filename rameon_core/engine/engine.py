from abc import ABC, abstractmethod
from typing import Any, Dict


class Engine(ABC):
    """
    Abstract base class for the Clarity Engine runtime.
    Defines the lifecycle and required behaviours for any engine implementation.
    """

    @abstractmethod
    def load(self, config: Dict[str, Any]) -> None:
        """
        Load engine configuration, domain packs, edition logic, and runtime components.
        """
        pass

    @abstractmethod
    def run(self, input_data: Any) -> Any:
        """
        Execute the engine pipeline on the provided input.
        """
        pass

    @abstractmethod
    def shutdown(self) -> None:
        """
        Cleanly shut down the engine, releasing resources and finalising state.
        """
        pass

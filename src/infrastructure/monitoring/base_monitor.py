"""
Base Monitor Interface.

All monitoring implementations must implement this interface.
"""

from abc import ABC, abstractmethod
from typing import Any, Optional


class BaseMonitor(ABC):
    """
    Abstract interface for monitoring and observability.

    Implementations can log LLM calls, tool executions, and other events
    to various observability platforms (Langfuse, W&B, etc.).
    """

    @abstractmethod
    def log_llm(
        self, prompt: str, response: str, metadata: Optional[dict[str, Any]] = None
    ) -> None:
        """
        Log LLM call.

        Args:
            prompt: Input prompt
            response: LLM response
            metadata: Additional metadata
        """
        pass

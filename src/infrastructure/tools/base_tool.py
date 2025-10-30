"""
Base Tool Interface.

All tools must implement this interface to be used by the agent.
Different LLM providers and frameworks have different tool representations,
so this is a minimal abstraction that can be adapted.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseTool(ABC):
    """
    Base interface for all tools.

    This is a minimal abstraction that can be adapted to different
    LLM provider formats (OpenAI functions, LangChain tools, LlamaIndex tools, etc.).
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Tool name."""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """
        Tool description for LLM.

        This description is used by LLM to decide when to use the tool.
        """
        pass

    @abstractmethod
    def execute(self, **kwargs) -> Any:
        """
        Execute the tool.

        Args:
            **kwargs: Tool-specific parameters

        Returns:
            Tool execution result (format depends on implementation)
        """
        pass

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert tool to dictionary representation.

        Different providers may need different formats:
        - OpenAI: function calling format
        - LangChain: tool format
        - LlamaIndex: tool format
        - etc.

        Returns:
            Dictionary representation of the tool
        """
        return {"name": self.name, "description": self.description}

"""
LLM Gateway - Abstract interface for LLM providers.

This port defines the contract for interacting with LLM providers,
allowing the core business logic to be independent of specific implementations.
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional, TypeVar, Type
from pydantic import BaseModel

T = TypeVar('T', bound=BaseModel)


class LLMGateway(ABC):
    """
    Abstract interface for LLM providers.
    
    All LLM adapters must implement this interface to be used
    by the core use cases.
    """
    
    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> str:
        """
        Generate text from a prompt.
        
        Args:
            prompt: The input prompt
            **kwargs: Additional parameters (temperature, max_tokens, etc.)
            
        Returns:
            Generated text response
        """
        pass
    
    @abstractmethod
    def embed(self, texts: List[str], **kwargs) -> List[List[float]]:
        """
        Generate embeddings for texts.
        
        Args:
            texts: List of texts to embed
            **kwargs: Additional parameters
            
        Returns:
            List of embedding vectors
        """
        pass
    
    def generate_structured(
        self,
        prompt: str,
        response_model: Type[T],
        **kwargs
    ) -> T:
        """
        Generate structured output using Pydantic model.
        
        Many LLM providers support structured output (OpenAI JSON mode,
        Anthropic structured outputs, etc.). This method should use
        provider-specific implementations.
        
        Args:
            prompt: Input prompt
            response_model: Pydantic model class for structured output
            **kwargs: Additional parameters
            
        Returns:
            Instance of response_model with structured data
            
        Raises:
            NotImplementedError: If provider doesn't support structured output
        """
        raise NotImplementedError(
            f"{self.__class__.__name__} does not support structured output"
        )
    
    def generate_with_functions(
        self,
        query: str,
        functions: List[Dict[str, Any]],
        system_prompt: Optional[str] = None,
        **kwargs
    ) -> Optional[Dict[str, Any]]:
        """
        Generate response with function calling support.
        
        This is an optional method for agents that support function calling.
        Default implementation returns None (no function call).
        
        Args:
            query: User query
            functions: List of function schemas (provider-specific format)
            system_prompt: Optional system prompt
            **kwargs: Additional parameters
            
        Returns:
            Function call dictionary or None if no function should be called
        """
        # Default implementation - can be overridden by specific adapters
        return None

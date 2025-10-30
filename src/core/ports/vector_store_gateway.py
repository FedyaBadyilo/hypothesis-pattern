"""
Vector Store Gateway - Abstract interface for vector databases.

This port defines the contract for interacting with vector stores,
allowing retrieval tools to work with any vector database implementation.
"""

from abc import ABC, abstractmethod
from typing import List
from src.core.domains.entities import Document


class VectorStoreGateway(ABC):
    """
    Abstract interface for vector store providers.

    Used by retrieval tools to search for relevant documents.
    Implementations should use existing vectorization tools.
    """

    @abstractmethod
    def search(self, query: str, top_k: int = 5, **kwargs) -> List[Document]:
        """
        Search for relevant documents by query.

        Args:
            query: Search query
            top_k: Number of results to return
            **kwargs: Additional search parameters

        Returns:
            List of relevant documents
        """
        pass

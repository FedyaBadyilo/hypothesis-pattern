"""
Domain entities - Core business objects.

These are pure data structures representing domain concepts,
independent of any external frameworks or infrastructure.
"""

from typing import Any, Optional

from pydantic import BaseModel, Field


class Document(BaseModel):
    """Represents a document in the system."""

    text: str
    id: Optional[str] = None
    metadata: Optional[dict[str, Any]] = Field(default_factory=dict)

"""
Domain entities - Core business objects.

These are pure data structures representing domain concepts,
independent of any external frameworks or infrastructure.
"""

from pydantic import BaseModel, Field
from typing import Dict, Any, Optional


class Document(BaseModel):
    """Represents a document in the system."""
    
    text: str
    id: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)

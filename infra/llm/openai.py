from __future__ import annotations

from typing import TYPE_CHECKING

from infra.config import get_config_and_env

if TYPE_CHECKING:
    from langchain_openai import ChatOpenAI


def get_openai_llm(model_name: str, config: dict | None = None) -> ChatOpenAI:
    """Build an OpenAI chat model from config MODELS[model_name]."""
    from langchain_openai import ChatOpenAI

    if config is None:
        config = get_config_and_env()
    llm_config = config["MODELS"][model_name]
    return ChatOpenAI(**llm_config)

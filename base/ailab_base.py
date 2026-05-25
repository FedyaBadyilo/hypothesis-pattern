from __future__ import annotations

import os
import logging
import yaml
from dotenv import load_dotenv
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from langchain_openai import ChatOpenAI

_current_file = Path(__file__).resolve()
_project_root = _current_file.parent.parent  # src/base -> src -> project_root

logger = logging.getLogger(__name__)

def config_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler()]
    )


def _resolve_config_path(config_path: str | os.PathLike[str]) -> Path:
    """Преобразует путь к конфигу в абсолютный (относительно корня проекта)."""
    path = Path(config_path)
    if path.is_absolute():
        return path
    return (_project_root / path).resolve()


def get_config_and_env(
    config_path: str | os.PathLike[str] = "config.yaml",
) -> dict:
    """Загружает конфиг из YAML и объединяет его с переменными окружения.

    Ключи из os.environ перекрывают одноимённые ключи из YAML на верхнем уровне.
    Вложенные структуры из YAML (например, MODELS.observer) сохраняются.
    """
    load_dotenv(_project_root / ".env")
    config_file = _resolve_config_path(config_path)
    with config_file.open(encoding="utf-8") as f:
        config = yaml.safe_load(f)

    if config is None:
        config = {}

    env = dict(os.environ)
    merged = {**config, **env}
    return merged


def get_openai_llm(model_name: str, config: dict | None = None) -> ChatOpenAI:
    """Получает и инициализирует модель OpenAI LLM из конфига"""
    from langchain_openai import ChatOpenAI

    if config is None:
        config = get_config_and_env()
    llm_config = config["MODELS"][model_name]

    return ChatOpenAI(**llm_config)


def create_langfuse_handler(
    enabled: bool,
    url: str,
    public: str,
    secret: str,
    debug: bool | None = False,
):
    import httpx
    from langfuse import Langfuse
    from langfuse.langchain import CallbackHandler

    if not enabled or url is None:
        return None

    logger.info(f"Langfuse URL set to '{url}'")

    if not public or not secret:
        logger.warning(
            f"Langfuse URL was specified, but '{public}' or '{secret}' was not, tracing disabled"
        )
        return None

    logger.info("Tracing enabled")

    # Чтобы обходить проверки SSL — необходимо передавать кастомный httpx клиент
    httpx_client = httpx.Client(verify=False, cert=None)
    try:
        Langfuse(
            host=url,
            secret_key=secret,
            public_key=public,
            debug=debug,
            httpx_client=httpx_client,
        )
        logger.info("Langfuse client initialized")
    except Exception as e:
        logger.error(f"Langfuse initialization failed: {e}")
        httpx_client.close()
        return None

    return CallbackHandler(public_key=public)


def get_langfuse_handler():
    """Создает Langfuse callback handler для трекинга LLM вызовов"""
    config = get_config_and_env()

    return create_langfuse_handler(
        enabled=bool(config.get("LANGFUSE_ENABLE", False)),
        url=config.get("LANGFUSE_HOST"),
        public=config.get("LANGFUSE_PUBLIC"),
        secret=config.get("LANGFUSE_SECRET"),
        debug=config.get("LANGFUSE_DEBUG", False),
    )






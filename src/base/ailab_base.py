import os

import yaml
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore


def get_config_and_env(config_path="src/config/default.yaml"):
    """Загружает конфиг из YAML и получает переменные окружения, объединяя их в один словарь"""
    with open(config_path, encoding="utf-8") as f:
        config = yaml.safe_load(f)
    env = dict(os.environ)
    merged = {**config, **env}
    return merged


CONFIG = get_config_and_env()


def get_openai_llm(model_name: str = "base_llm", config: dict | None = None) -> ChatOpenAI:
    """Получает и инициализирует модель OpenAI LLM из конфига"""
    if config is None:
        config = CONFIG
    llm_config = config["MODELS"][model_name]

    return ChatOpenAI(**llm_config)


def get_openai_embedder(
    model_name: str = "base_embedder", config: dict | None = None
) -> OpenAIEmbeddings:
    """Получает и инициализирует OpenAI эмбеддер из конфига"""

    if config is None:
        config = CONFIG
    embedder_config = config["MODELS"][model_name]

    return OpenAIEmbeddings(**embedder_config)


def get_qdrant_vector_store(
    embedding: OpenAIEmbeddings | None = None, config: dict | None = None
) -> QdrantVectorStore:
    """Получает и инициализирует Qdrant vector store из конфига"""

    if config is None:
        config = CONFIG
    vector_store_config = config["VECTOR_STORE"]
    collection = vector_store_config["collection"]

    if collection:
        if embedding is None:
            embedding = get_openai_embedder(config=config)

        return QdrantVectorStore.from_existing_collection(
            collection_name=collection, embedding=embedding, **vector_store_config
        )
    else:
        raise ValueError("Collection is not set in the config")

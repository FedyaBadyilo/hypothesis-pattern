# LLM Hypothesis Template

A standardized template repository for rapid prototyping and hypothesis testing
of LLM-powered agents, RAG systems, and document processing solutions.

## Purpose

This template provides a unified, simple, and efficient architecture for creating
prototypes to validate hypotheses about LLM integration for various business cases.
It follows the principle of "one structure, many hypotheses" - clone, configure, and iterate.

## Architecture

The template follows Clean Architecture principles with dependency inversion:

- **Core**: Business logic independent of external services
  - `domains/entities.py` - Domain models (Pydantic)
  - `ports/` - Abstract interfaces (LLM gateway, vector store gateway)
  
- **Infrastructure**: Adapters for external services
  - `llm/` - LLM provider adapters (OpenAI, Yandex, etc.)
  - `tools/` - Tool implementations (base interface)
  - `monitoring/` - Observability adapters
  - `vector_db/` - Vector store adapters (to be implemented)

- **Applications**: Entry points
  - `cli/` - Command-line interface
  - `api/` - REST API (FastAPI)

- **Custom**: Domain-specific logic for specific hypotheses
  - `domain_specific/` - Domain-specific components
  - `business_rules/` - Business rules
  - `utils/` - Utility functions

## Getting Started

1. Clone this template
2. Configure `src/config/default.yaml`
3. Add your API keys to `.env`
4. Implement your hypothesis-specific code

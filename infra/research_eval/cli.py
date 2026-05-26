import argparse
from typing import Type

from infra.research_eval.runner import evaluate_experiment
from infra.research_eval.types import BaseEvalAdapter


def run_eval_cli(adapter_cls: Type[BaseEvalAdapter]) -> None:
    parser = argparse.ArgumentParser(description="Run step evaluation experiment")
    parser.add_argument("--source", required=True, help="Evaluation input (opaque to baseline)")
    parser.add_argument("--name", required=True, help="MLflow run name")
    args = parser.parse_args()

    evaluate_experiment(
        adapter_cls=adapter_cls,
        source=args.source,
        name=args.name,
    )

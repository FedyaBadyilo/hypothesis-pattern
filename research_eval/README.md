# research_eval

Минимальное переиспользуемое ядро оценки для research-пайплайна: контракт адаптера, orchestration прогона и логирование в MLflow.

Доменные метрики и разбор `--source` остаются в `steps/<step>/eval/adapter.py`.

## Установка

```bash
pip install -r requirements.research.txt
pip install -r requirements.txt
```

`research_eval/tracking.py` загружает env через `base/ailab_base.get_config_and_env()` — для этого нужны зависимости из основного `requirements.txt`.

Скопируйте `.env.example` в `.env` и задайте `MLFLOW_TRACKING_URI` для реальных прогонов.

## Контракт

- `EvalResult` — Pydantic-модель: `metrics: dict[str, float]`, `artifacts: dict[str, Any]`
- `BaseEvalAdapter` — ABC с `target: ClassVar[str]` и `evaluate(source) -> EvalResult`
- MLflow **experiment** = `adapter_cls.target`
- MLflow **run name** = CLI `--name`

## Подключение шага

`steps/stepN/eval/adapter.py`:

```python
from pathlib import Path

from research_eval.types import BaseEvalAdapter, EvalResult


class StepNEvalAdapter(BaseEvalAdapter):
    target = "stepN"

    def evaluate(self, source: str | Path) -> EvalResult:
        ...
```

`steps/stepN/eval/run.py`:

```python
from research_eval.cli import run_eval_cli

from steps.stepN.eval.adapter import StepNEvalAdapter

if __name__ == "__main__":
    run_eval_cli(adapter_cls=StepNEvalAdapter)
```

## Запуск

Из корня репозитория (после добавления `adapter.py` и `run.py` в шаге):

```bash
python -m steps.stepN.eval.run --source <source> --name <mlflow-run-name>
```

Аргументы:

- `--source` — opaque input (передаётся в адаптер как есть)
- `--name` — имя MLflow run

Шаблон eval для шага — в [steps/step1/eval/README.md](../steps/step1/eval/README.md).

## Артефакты в MLflow

| Значение в `artifacts[key]` | Поведение |
|---|---|
| путь к существующему файлу | логируется файл (при необходимости копия с именем `key`) |
| `dict` / `list` / scalar | сериализация в JSON с именем файла `key` |

# [название гипотезы]

## Гипотеза
<!-- Краткое описание: что проверяем, зачем, в каких условиях -->

## Решение (верхний уровень)
<!-- Кратко: общий подход, основные компоненты, как гипотеза реализована в коде -->

## Структура репозитория

- `infra/` — переиспользуемая инфраструктура (config, LLM, eval runner, файловые хелперы)
- `research/` — код гипотезы: `datasets/`, `lab/`, `steps/<step_name>/`
- `apps/` — приложения и демо (когда появятся)
- `config.yaml` — конфигурация (модели, ключи и т.п.)

## Запуск по шагам
<!-- Перечислите порядок и команды. Пример: -->

1. **Предобработка данных** (если нужна): см. `research/datasets/build/README.md`

2. **Шаг** `step_name`: см. `research/steps/step_name/README.md`

3. **Оценка шага** (eval): см. `infra/research_eval/README.md` — добавьте `eval/adapter.py` и `eval/run.py` в шаг, когда метрики будут нужны.

## Требования

- Python 3.x
- Зависимости: `pip install -r requirements.txt` и `pip install -r requirements.research.txt`
- Переменные окружения: скопировать `.env.example` в `.env` и заполнить

## Документация

- **Новая гипотеза из шаблона** — [docs/common/new-hypothesis-from-template.md](docs/common/new-hypothesis-from-template.md) (создание репозитория на GitLab Community)
- Описание шага — `research/steps/<step_name>/README.md`
- Shared eval core — `infra/research_eval/README.md`

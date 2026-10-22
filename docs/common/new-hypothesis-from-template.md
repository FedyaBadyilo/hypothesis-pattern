# Новая гипотеза из шаблона (GitLab Community)

На GitLab Community нет custom project templates. Новый репозиторий создаём через Git: копируем файлы шаблона локально и пушим в **пустой** проект гипотезы.

## Репозиторий-шаблон

| Способ | URL                                                   |
| ------ | ----------------------------------------------------- |
| SSH    | `ssh://git@gitlab.rosatom.local:2222/source/gren-tsii/aspii-team/aspii-system/hypotheses/templates/hypothesis-pattern.git`     |
| HTTPS  | `https://gitlab.rosatom.local/source/gren-tsii/aspii-team/aspii-system/hypotheses/templates/hypothesis-pattern.git` |


## Что понадобится

- Доступ на **чтение** к репозиторию
- Права на **запись** в группу, в которой создаете репозиторий для гипотезы
- Локально: `git`, SSH или HTTPS к `gitlab.rosatom.local`

В командах значения в угловых скобках `<...>` — плейсхолдеры: подставьте свои, скобки в команду не копируйте.

- `<HYPOTHESIS_URL>` — URL **нового** проекта (например `git@git.gitlab.rosatom.local/source/gren-tsii/aspii-team/aspii-system/hypotheses/<my-hypothesis>.git`)
- `<my-hypothesis>` — имя локальной папки

## 1. Пустой проект в GitLab

**New project → Create blank project**

- Укажите группу и имя проекта
- **Снимите** «Initialize repository with a README» — репозиторий должен быть пустым

Скопируйте URL нового проекта — это `<HYPOTHESIS_URL>`.

## 2. Клонировать шаблон и отвязать от него

```bash
git clone --depth 1 ssh://git@gitlab.rosatom.local:2222/source/gren-tsii/aspii-team/aspii-system/hypotheses/templates/hypothesis-pattern.git <my-hypothesis>
cd <my-hypothesis>

rm -rf .git
git init
git branch -M main
git add -A
git commit -m "Initial commit from HyppoPattern template"
```

Через HTTPS:

```bash
git clone --depth 1 https://gitlab.rosatom.local/source/gren-tsii/aspii-team/aspii-system/hypotheses/templates/hypothesis-pattern.git <my-hypothesis>
```

`--depth 1` — только последний снимок файлов, без истории шаблона.

## 3. Привязать к репозиторию гипотезы и запушить

```bash
git remote add origin <HYPOTHESIS_URL>
git push -u origin main
```

После push в GitLab появятся файлы и ветка `main`. Шаблон `ailab/hypopattern` на сервере не меняется.

## 4. Настройка после создания

| Действие                          | Зачем                                 |
| --------------------------------- | ------------------------------------- |
| Обновить `README.md`              | Название и описание гипотезы          |
| `.env.example` → `.env`           | Ключи и секреты (`.env` не коммитить) |
| При необходимости — `config.yaml` | Модели и пути под задачу              |

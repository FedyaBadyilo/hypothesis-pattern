# Новая гипотеза из шаблона (GitLab Community)

На GitLab Community нет custom project templates. Новый репозиторий создаём через Git: копируем файлы шаблона локально и пушим в **пустой** проект гипотезы.

## Репозиторий-шаблон

Проект: `ailab/hypopattern`

| Способ | URL                                                   |
| ------ | ----------------------------------------------------- |
| SSH    | `git@git.cifrum-digital.ru:ailab/hypopattern.git`     |
| HTTPS  | `https://git.cifrum-digital.ru/ailab/hypopattern.git` |


## Что понадобится

- Доступ на **чтение** к `ailab/hypopattern`
- Права на **запись** в группу, куда создаёте гипотезу
- Локально: `git`, SSH или HTTPS к `git.cifrum-digital.ru`

Замените в командах только:

- `HYPOTHESIS_URL` — URL **нового** проекта (например `git@git.cifrum-digital.ru:ailab/my-hypothesis.git`)
- `my-hypothesis` — имя локальной папки

## 1. Пустой проект в GitLab

**New project → Create blank project**

- Укажите группу и имя проекта
- **Снимите** «Initialize repository with a README» — репозиторий должен быть пустым

Скопируйте URL нового проекта — это `HYPOTHESIS_URL`.

## 2. Клонировать шаблон и отвязать от него

```bash
git clone --depth 1 git@git.cifrum-digital.ru:ailab/hypopattern.git my-hypothesis
cd my-hypothesis

rm -rf .git
git init
git branch -M main
git add -A
git commit -m "Initial commit from HyppoPattern template"
```

Через HTTPS:

```bash
git clone --depth 1 https://git.cifrum-digital.ru/ailab/hypopattern.git my-hypothesis
```

`--depth 1` — только последний снимок файлов, без истории шаблона.

## 3. Привязать к репозиторию гипотезы и запушить

```bash
git remote add origin HYPOTHESIS_URL
git push -u origin main
```

Пример, если гипотеза — `ailab/my-hypothesis`:

```bash
git remote add origin git@git.cifrum-digital.ru:ailab/my-hypothesis.git
git push -u origin main
```

После push в GitLab появятся файлы и ветка `main`. Шаблон `ailab/hypopattern` на сервере не меняется.

## 4. Настройка после создания

| Действие                          | Зачем                                 |
| --------------------------------- | ------------------------------------- |
| Обновить `README.md`              | Название и описание гипотезы          |
| `.env.example` → `.env`           | Ключи и секреты (`.env` не коммитить) |
| При необходимости — `config.yaml` | Модели и пути под задачу              |

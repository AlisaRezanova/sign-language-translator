# 🤟 Sign Language Translator

Система перевода **русского жестового языка (РЖЯ)** в текст для **медицинского контекста**
(приём в поликлинике и др.). Компьютерное зрение распознаёт жесты, LLM собирает из них
грамматически корректную фразу с учётом медицинской терминологии.

## Архитектура

```
видео → MediaPipe (ключевые точки) → модель жестов → [список жестов] → LLM + глоссарий → текст
         └──────────────── cv/ ─────────────────┘                     └──── nlp/ ────┘
                                    app/ (FastAPI)
```

## Структура

| Папка        | Что внутри                                  |
|--------------|---------------------------------------------|
| `app/`       | FastAPI backend (эндпоинты)                 |
| `cv/`        | Извлечение ключевых точек, модели жестов    |
| `nlp/`       | Промпты, интеграция с LLM, глоссарий        |
| `data/`      | Датасеты (не коммитятся)                    |
| `notebooks/` | Эксперименты                                |
| `docs/`      | Статья, материалы для патента               |
| `tests/`     | Тесты                                       |

## Быстрый старт

```bash
python -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
pre-commit install

uvicorn app.main:app --reload        # http://localhost:8000/docs
pytest
```

Через Docker:

```bash
docker build -t slt .
docker run -p 8000:8000 slt
```

## Команда

- **Человек А** — backend, NLP/LLM, интеграция
- **Человек Б** — данные, CV-модели

Задачи ведём на [доске GitHub Projects](https://github.com/users/AlisaRezanova/projects/6).

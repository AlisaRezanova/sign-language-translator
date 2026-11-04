"""FastAPI backend: точка входа API переводчика РЖЯ."""

from fastapi import FastAPI

app = FastAPI(
    title="Sign Language Translator API",
    description="Перевод русского жестового языка (РЖЯ) в текст для медицинского контекста.",
    version="0.1.0",
)


@app.get("/")
def root() -> dict:
    return {"message": "Hello from Sign Language Translator!"}


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}

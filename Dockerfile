FROM python:3.9-slim

RUN pip install poetry

ENV PATH=/root/.local/bin:$PATH

COPY pyproject.toml poetry.lock ./

COPY poetry.lock ./poetry.lock
RUN poetry install --no-interaction

COPY docker_fastapi ./docker_fastapi
RUN pip install uvicorn
# CMD ["uvicorn", "main:app", "--reload"]

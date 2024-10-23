FROM python:3.10-slim as builder


RUN pip install --no-cache-dir poetry==1.5.1
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /code
COPY ./poetry.lock ./pyproject.toml ./
RUN touch README.md
RUN poetry install --only main --no-root && rm -rf $POETRY_CACHE_DIR

FROM python:3.10-slim as runner

ENV VIRTUAL_ENV=/code/.venv \
    PATH="/code/.venv/bin:${PATH}" \
    PYTHONPATH="${PYTHONPATH}:/code"

RUN apt-get update && \
    apt-get install -y \
    libxext6 ffmpeg -y && \
    rm -rf /var/lib/apt/lists/*

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

WORKDIR code/
COPY app app

EXPOSE 80

# Start the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
FROM python:3.9-slim as base

RUN apt-get update && apt-get install -y gcc libffi-dev g++ curl
WORKDIR /app

FROM base as builder

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

RUN python -m venv /venv

COPY . .

RUN . /venv/bin/activate && poetry install --no-dev --no-root

RUN . /venv/bin/activate && poetry build -f wheel && pip install -U dist/*.whl


FROM base as final

COPY --from=builder /venv /venv

ENTRYPOINT ["/venv/bin/python", "-m", "testmoretv"]
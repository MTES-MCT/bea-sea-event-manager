FROM python:3.10-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY pyproject.toml poetry.lock /app/
RUN pip install poetry
RUN poetry install
COPY ./src/ /app/src/
CMD ["poetry", "run", "python", "/app/src/manage.py", "runserver", "0.0.0.0:8000"]


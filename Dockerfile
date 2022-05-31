FROM python:3.10-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY pyproject.toml poetry.lock /code/
RUN pip install poetry
RUN poetry install
COPY ./sea_events_manager/ /code/
COPY ./.env /code/
RUN ls
CMD ["poetry", "run", "python", "/code/manage.py", "runserver", "0.0.0.0:8000"]

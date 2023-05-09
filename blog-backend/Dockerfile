FROM python:3.10.11-alpine3.17

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY . .

RUN python manage.py makemigrations \
  && python manage.py migrate

CMD ["gunicorn backend.wsgi:application --bind 0.0.0.0:8000"]

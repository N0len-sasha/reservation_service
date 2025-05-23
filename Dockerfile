FROM python:3.13

WORKDIR /app

COPY pyproject.toml poetry.lock* ./
RUN pip install --no-cache-dir poetry \
 && poetry config virtualenvs.create false \
 && poetry install --no-root

COPY . .

CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:8000", "reservation_service_API.wsgi:application"]
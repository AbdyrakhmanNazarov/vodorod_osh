# Используем Python 3.11 Slim
FROM python:3.11-slim

# Отключаем запись pyc и буферизацию stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Обновляем пакетный менеджер и устанавливаем psycopg2 dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*

# Копируем только requirements.txt сначала, чтобы кешировать установку
COPY requirements.txt /app/

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . /app

# Документируем порт
EXPOSE 8002

# Запуск Django на 8002
CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]










# # Второй вариант
# # Используем Python 3.11 на Alpine
# FROM python:3.11-alpine3.16

# # Отключаем запись pyc и буферизацию stdout/stderr
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# WORKDIR /app

# # Сначала копируем только requirements, чтобы ускорить сборку при изменениях кода
# COPY requirements.txt /app/

# # Устанавливаем зависимости и необходимые пакеты для PostgreSQL
# RUN apk add --no-cache postgresql-client build-base postgresql-dev \
#     && pip3 install --no-cache-dir -r requirements.txt

# # Копируем весь проект
# COPY . /app

# # Документируем, что контейнер слушает 8002
# EXPOSE 8002

# # Запуск Django на порту 8002
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]

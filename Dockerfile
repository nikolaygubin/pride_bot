# Устанавливаем версию питона и используемы linux дистрибутив
# Alpine легковесный дистрибутив Linux
FROM python:3-alpine

# Устанавливаем нужные приложению зависимости
RUN \
 apk add --no-cache python3 postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
 pip install setuptools==68.2.2 && \
 pip install psycopg2-binary --no-cache-dir && \
 pip install psycopg2 && \
 apk --purge del .build-deps

# Cоздаем директорию, где будет размещено приложение
RUN mkdir /app
WORKDIR /app

# Копируем файлы приложения и запускаем установку пакетов
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY . /app

# При запуске контейнера будет выполнен этот скрипт.
CMD python /app/telegram_bot.py
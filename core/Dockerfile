FROM python:3.8

WORKDIR /app


RUN apt-get update && \
    apt-get install -y postgresql-client

WORKDIR /app

COPY . /app/core
COPY ./initDB.py /app

RUN pip install psycopg2

ENV POSTGRES_HOST=<localhost>
ENV POSTGRES_PORT=<5432>
ENV POSTGRES_DB=<postgres>
ENV POSTGRES_USER=<postgres>
ENV POSTGRES_PASSWORD=<postgres>

CMD ["python", "initDB.py"]

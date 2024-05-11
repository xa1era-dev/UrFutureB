FROM python:3.11-alpine
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install --upgrade pip && pip install -r requirements.txt && rm -rf ~/.cache/pip
COPY . /app
EXPOSE 8080
CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8080"]
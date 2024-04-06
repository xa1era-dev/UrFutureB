# UrFutureB

## To install
```
Python 3.11
Postgress - ??
```

> [!CAUTION]
> Нужно запросить файл `.env` для работы сервера.

> [!IMPORTANT]
> Для того, чтобы вместе с [апи поднять](#%D0%BF%D0%BE%D0%B4%D0%BD%D1%8F%D1%82%D0%B8%D0%B5-%D1%81%D0%B5%D1%80%D0%B2%D0%B5%D1%80%D0%B0) сервер, нужно в папку `\static` запулить данный [репозиторий](https://github.com/xa1era-dev/UrFutureF) фронта

## Установка venv
  Ставим виртуальное окружение в папку, где находится репозиторий `python3 -m venv .venv`.
  
  После активируем venv `.venv\Scripts\activate.bat`.
  
  После загружаем все либы в наш venv `pip install -r requirements.txt`.


## Поднятие сервера
 Нужно из активированного venv вызвать данную команду `uvicorn main:app --reload`

 > `--reload` - Любые изменения, сделанные в файлах проекта, перезапустят сервер. Не рекомендуется при разработке фронта.

 ## Тестирование запросов
После запуска сервера, на `http://localhost:8000/docs` будет находиться Swagger.



> [!NOTE]
> Для удобного менеджемтна запросов, сделать генератор ссылок:
> ``` `${host}${href}` ``` 
> - host - const итоговый хост. Можно получить при помощи new URL(this.window.location).host
> - href - эндпоинт.

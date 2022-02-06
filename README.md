# Overview
Максимально простой балансировщик видео-трафика

Осуществляет перенаправление каждого десятого запроса.


## Docker
Для запуска проекта с помощью [Docker](https://www.docker.com/) необходимо:
1. В docker-compose.yml указать корректное значение `CDN_HOST` - требуемый url сервиса CDN 
(по умолчанию установлен `more.tv`) 
2. Затем выполнить следующую команду:
`docker-compose up`

## Run Local
Для запуска проекта вне контейнера потребуется:
1. Установить [poetry](https://python-poetry.org/). Один из вариантов:
`pip install --user poetry`
2. Установить зависимости:
`poetry install`
3. Запустить сервис:
    1. Выставить переменную окружения `CDN_HOST`: `export CDN_HOST=more.tv`
    2. Запустить сервис `poetry run moretv`

## Example
Пример запроса:
curl - GET http://127.0.0.1:8000/?video=http://s1.origin-cluster/video/1488/xcg2djHckad.m3u8


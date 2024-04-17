# Funtech_backend

[![CI/CD](https://github.com/Team88888/Funtech_backend/actions/workflows/ci_cd.yml/badge.svg)](https://github.com/Team88888/Funtech_backend/actions/workflows/ci_cd.yml)

Проект развернут на сервере:<br>
https://funtech-team8.duckdns.org/api/v1/ <br>
https://funtech-team8.duckdns.org/api/v2/ <br>

  Мониторинг фоновых задач Celery осуществляется по адресу: http://funtech-team8.duckdns.org:5555/ .

  Для активации фоновых задач необходимо выполнить GET-запрос к эндпойнтам:
  - специализаций (http://funtech-team8.duckdns.org/api/v2/specializations/?theme=3)
  - стека (http://funtech-team8.duckdns.org/api/v2/stack/?specialization=4)

  Администрирование приложения может быть осуществлено:
  - через админ панель по адресу https://funtech-team8.duckdns.org/admin<br>
      <a href="#t1">Учетные данные</a> для входа в админ-зону
  - через Swagger доступный по адресу https://funtech-team8.duckdns.org/docs

  Техническая документация:
  - Redoc доступен по адресу https://funtech-team8.duckdns.org/redoc
  - Скачать yaml-файл можно по адресу https://funtech-team8.duckdns.org/schema

<br>

## Оглавление
- [Технологии](#технологии)
- [Установка приложения](#установка-приложения)
- [Запуск тестов](#запуск-тестов)
- [Запуск приложения](#запуск-приложения)
- [Удаление приложения](#удаление-приложения)
- [Авторы](#авторы)

<br>

## Технологии
<details><summary>Подробнее</summary><br>

[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue?logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.0-blue?logo=Django)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/-djangoRESTframework-464646?logo=djangorestframework)](https://www.django-rest-framework.org/)
[![drf-spectacular](https://img.shields.io/badge/-drf--spectacular-464646?logo=drfspectacular)](https://drf-spectacular.readthedocs.io/en/latest/)
[![celery](https://img.shields.io/badge/-Celery-464646?logo=celery)](https://docs.celeryq.dev/en/stable/)
[![rabbitmq](https://img.shields.io/badge/-RabbitMQ-464646?logo=rabbitmq)](https://www.rabbitmq.com/)
[![flower](https://img.shields.io/badge/-Flower-464646?logo=flower)](https://flower.readthedocs.io/en/latest/)
[![docker_compose](https://img.shields.io/badge/-Docker%20Compose-464646?logo=docker)](https://docs.docker.com/compose/)
[![Pytest](https://img.shields.io/badge/-pytest-464646?logo=Pytest)](https://docs.pytest.org/en/latest/)
[![Pytest-django](https://img.shields.io/badge/-pytest--django-464646?logo=Pytest)](https://pytest-django.readthedocs.io/en/latest/index.html)
[![pytest-cov](https://img.shields.io/badge/-pytest--cov-464646?logo=codecov)](https://pytest-cov.readthedocs.io/en/latest/)
[![factoryboy](https://img.shields.io/badge/-factoryboy-464646?logo=factoryboy)](https://factoryboy.readthedocs.io/en/stable/index.html)
[![pre-commit](https://img.shields.io/badge/-pre--commit-464646?logo=pre-commit)](https://pre-commit.com/)

[⬆️Оглавление](#оглавление)

</details>

<br>

## Установка приложения:

<details><summary>Предварительные условия</summary>

Предполагается, что пользователь установил [Docker](https://docs.docker.com/engine/install/) и [Docker Compose](https://docs.docker.com/compose/install/) на локальной машине. Проверить наличие можно выполнив команды:

```bash
    docker --version && docker-compose --version
```
</details>

<br>

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=250&width=435&lines=Для+пользователей+Windows:)](https://github.com/alexpro2022)

**!!! обязательно выполнить команду:** иначе файл start.sh при клонировании будет бракован:
```bash
    git config --global core.autocrlf false
```
<br><br>

Клонируйте репозиторий с GitHub и введите данные для переменных окружения (значения даны для примера, но их можно оставить):

```bash
    git clone https://github.com/Team88888/Funtech_backend.git
    cd Funtech_backend
    cp env_example .env
    nano .env
```

[⬆️Оглавление](#оглавление)

<br>

## Запуск тестов:
#### (Виртуальное окружение) Codecov=97%

1. Создайте и активируйте виртуальное окружение и установите необходимые зависимости::
   * Если у вас Linux/macOS
   ```bash
    python -m venv venv && source venv/bin/activate
    python -m pip install --upgrade pip && pip install -r requirements/test.requirements.txt
   ```
   * Если у вас Windows
   ```bash
    python -m venv venv && source venv/Scripts/activate
    python -m pip install --upgrade pip && pip install -r requirements/test.requirements.txt
   ```

2. Из корневой директории проекта выполните команду:
```bash
    python funtech_proj/manage.py makemigrations
    pytest --cov --cov-config=.coveragerc
```

[⬆️Оглавление](#оглавление)

<br>

## Запуск приложения:
#### (Docker)

1. Из корневой директории проекта выполните команду:
```bash
    docker compose -f infra/local/docker-compose.yml --env-file .env up -d --build
```
  Проект будет развернут в docker-контейнерах по адресу <br>
  http://localhost/api/v1 <br>
  http://localhost/api/v2 <br>

  Мониторинг фоновых задач Celery осуществляется по адресу: http://localhost:5555/ .

  Для активации фоновых задач необходимо выполнить GET-запрос к эндпойнтам:
  - специализаций (http://localhost/api/v2/specializations/?theme=3)
  - стека (http://localhost/api/v2/stack/?specialization=4)

  Администрирование приложения может быть осуществлено:
  - через админ панель по адресу http://localhost/admin
  - через Swagger доступный по адресу http://localhost/docs

  Техническая документация:
  - Redoc доступен по адресу http://localhost/redoc
  - Скачать yaml-файл можно по адресу http://localhost/schema

<h4 id="t1">Учетные данные для входа в админ-зону:</h4>
<ul>
  <li>login: adm@adm.com
  <li>password: admpw
</ul><br>

2. Остановить docker и удалить контейнеры можно командой из корневой директории проекта:

```bash
    docker compose -f infra/local/docker-compose.yml --env-file .env down
```

Если также необходимо удалить том базы данных:
```bash
    docker compose -f infra/local/docker-compose.yml --env-file .env down -v && docker system prune -f
```

[⬆️Оглавление](#оглавление)

<br>

## Удаление приложения:
Из корневой директории проекта выполните команду:
```bash
    cd .. && rm -fr Funtech_backend && deactivate
```

[⬆️Оглавление](#оглавление)

<br>

## Авторы (в алфавитном порядке):

[Аустер Яков](https://github.com/find-y)<br>
[Варивода  Георгий](https://github.com/gerich02)<br>
[Проскуряков Алексей](https://github.com/alexpro2022)

[⬆️В начало](#funtech_backend)

# kafka-air-redis-learn

## Старт и остановка kaf стека

1. Перейдите в `cd kaf/app`
2. Установите `poetry` окружение и подготовьте линтер. Для этого используйте `poetry config virtualenvs.in-project true` и команду `poetry install --with dev`
3. Для vscode создайте проект `code .` в корне репозитория и укажите путь к нтерпретатору. Перезапустиие IDE.
4. Внутри контейнера можно выполнить:

    - `pytest -v -s -x` для тестирования
    - используйте `python -m IPython` для проверок кода
    - `mypy --install-types`
    - `mypy app` и `flake8 app`

5. `make serve-kaf` для запуска dev-стека
6. `make down-kaf` остановка и удаление стека
7. пересобрать отдельный сервис можно так `docker compose up -d --no-deps --build <service-name>`
8. [api swagger docs](http://localhost:8392/docs/)

## Ресурсы

- [kafka-python](https://kafka-python.readthedocs.io/en/master/)
- [aiokafka](https://github.com/aio-libs/aiokafka)
- [Faust](https://faust-streaming.github.io/faust/)
- [zookeeper](https://hub.docker.com/_/zookeeper)
- [art1](https://habr.com/ru/articles/578916/)
- [art2](https://habr.com/ru/articles/587592/)
- [art3](https://habr.com/ru/companies/slurm/articles/735262/)
- [bitnami kafka](https://hub.docker.com/r/bitnami/kafka)
- [what is the difference between bitnami/kafka and confluentinc/cp-kafka](https://stackoverflow.com/questions/73382919/what-is-the-difference-between-bitnami-kafka-and-confluentinc-cp-kafka)
- [test](https://docs.google.com/document/d/1K-HOOWGPTGjCafT6McC-7_dtjlWYQGro/edit)

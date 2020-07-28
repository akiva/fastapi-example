# FastAPI example

## Build the image and start container

```sh
docker-compose up -d --build
```

## Run the tests

```sh
docker-compose exec web pytest .
```

## Run the test coverage

```sh
docker-compose exec web coverage run -m pytest
```

## Run the test coverage reports

```bash
docker-compose exec web coverage report -m
```

## Connect to the database

```sh
docker-compose exec db psql --username=hello_fastapi --dbname=hello_fastapi_dev
```

## Watch logs as you develop

```sh
docker-compose logs -f
```

## Use cURL or HTTPie to test:

```sh
http --json POST http://localhost:8002/notes/ title=foo description=bar
```

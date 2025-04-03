# python-server-demo


## Preparation

Install [mise](https://formulae.brew.sh/formula/mise#default) to manage the env

```sh
mise install
pre-commit install
```

## Dev

> Copy `.env.dev` to `.env`, and update the value if you need


### Start DB

```sh
docker-compose up -d db
```
### Install deps
```sh
uv venv .venv
source .venv/bin/activate
uv pip install -r requirements.txt
uv pip install -e .
```

###  Start server

```sh
#Migrate db schema
flask db upgrade
# Start the app
start
# uninstall if needed
uv pip uninstall python-server-demo
```

## Other useful scripts

### Migration

```sh
# Generate migration scripts
flask db migrate -m "migration msg"
# Deploy the migration scripts
flask db upgrade
```

### Lint & Fix

```sh
uvx ruff check
uvx ruff format
uvx ruff check --fix
```

### Update deps

```sh
uv pip uninstall python-server-demo
uv pip freeze > requirements.txt
```

### Docker

```sh
docker build -t python-server-demo .
docker run -d \
  -p 6543:8080 \
  -e DATABASE_URL=postgresql://postgres:password@host.docker.internal:5432/python-server-demo \
  --name python-server-demo \
  python-server-demo
```

### Verify

```sh
# health
curl 'http://127.0.0.1:6543/api/v1/health'

# New cases
curl 'http://127.0.0.1:6543/api/v1/cases' \
  -H 'content-type: application/json' \
  -H 'x-api-key: dev-key' \
  --data-raw '{"name": "test"}'

```

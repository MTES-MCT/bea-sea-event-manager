# sea-event-manager-bea

Entry assistance tool for BEAMer investigators to the EMCIP database.


# Requirements:
- `Python 3.10+`
- `poetry`

# Installation
1) In the root folder install with poetry

```bash
poetry install
```

2) Configure the app with `.env` config file
=> To create a default `.env` config file:
```bash
echo 'SEA_EVENT_MANAGER_ALLOWED_HOSTS = "127.0.0.1,localhost,host.docker.internal"' > .env
```

3) Run the app (default to port 8000):

```bash
poetry run python3 sea_events_manager/manage.py runserver
```

# Reverse-proxy
If a reverse-proxy is desired, a functionnal dockerized setup is available in `.nginx` folder.

# Deploy with docker
## Requirements:
- `Docker`

## If build is needed:
```bash
docker build . -t sea_events_manager
```

## Run the app:
```bash
docker run -d -p 8000:8000 sea_events_manager
```

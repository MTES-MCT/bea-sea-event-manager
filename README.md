# sea-event-manager-bea
## Purpose
The purpose of this project is to ease the reporting of national sea events by the "BEA Mer" to the european sea event database EMCIP (owned by EMSA).

## Main features:
- Gather all sea events as reported by the CROSS to the BEA Mer
- Allow the user to discard a sea event as "ignored" if it is not relevant to the EMCIP database
- Allow the user to push as much information as possible to the EMCIP database (as a draft report) before completing the input in EMCIP UI.
- Allow the user to explore ignored and pushed reports from the app.

# Deploying the app
## Requirements
`Docker`

## Configuration
Configure the app with `.env` config file
=> To create a default `.env` config file:
```bash
echo 'SEA_EVENT_MANAGER_ALLOWED_HOSTS="127.0.0.1,localhost,host.docker.internal"
SEA_EVENT_MANAGER_DEBUG=False
SEA_EVENT_MANAGER_EMCIP_URL=https://apimgr-pp.emsa.europa.eu/services/emcip/v1
SEA_EVENT_MANAGER_BASIC_AUTHORIZATION_TOKEN=
SEA_EVENT_MANAGER_SECRET_KEY=
SEA_EVENT_MANAGER_STATIC_ROOT=/var/www/django_app
SEA_EVENT_MANAGER_FORCE_SCRIPT_NAME=
SEA_EVENT_MANAGER_NB_ITEM_PER_PAGE=10
RAW_REPORTS_DB_USERNAME=raw_reports_user
RAW_REPORTS_DB_PASSWORD=raw_reports_pwd
RAW_REPORTS_DB_HOST=localhost
RAW_REPORTS_DB_PORT=5432
RAW_REPORTS_DB_DATABASE=raw_reports_db'> .env
```

## If build is needed:
```bash
docker build . -t <project_docker_hub_id>/sea_events_manager
```

## Run the app:
Generate a valid `.env` file and provide it to the container with -v option.

Static files are exposed through a volume mounted in the container.

```bash
docker run \
-d --rm \
-p 8000:8000 \
-v /path/to/local/db.sqlite3:/app/db.sqlite3 \
-v /var/www/django_app/static/:/app/src/static_root/static/ \
--env-file=.env \
--name=django_app <project_docker_hub_id>/sea_events_manager

docker exec django_app poetry run python /app/src/manage.py collectstatic --noinput
```

# Reverse-proxy
If a reverse-proxy is desired, a functionnal dockerized setup is available in `.nginx` folder.

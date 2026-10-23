# Location cache demo (Django)

Small Django app with a location form whose lookup is meant to be cached in Redis.

> Status: minimal runnable version. Parts that were incomplete are marked with `TODO` in the code; external services are mocked.

## Quick start (Docker)

```sh
make docker-run        # builds the image and serves http://localhost:8000
```

## Quick start (local Python 3.8)

```sh
make setup             # creates .venv and installs requirements.txt
make run               # migrates SQLite and serves http://localhost:8000
make superuser         # optional: admin user for /admin
```

## Offline demo (no Django)

`demo.py` is a standalone geocode-plus-cache demo: run `python3 demo.py`, or `docker build -f Dockerfile.demo -t django-demo . && docker run --rm django-demo`. `TODO.md` lists follow-up work. Its first two items (POST parsing, `cache.get`/`cache.set`) are now fixed in `api/views.py`.

## Mocks

Controlled by `USE_MOCKS` (default `1`), added at the end of `cred/settings.py`:

- Redis cache replaced by an in-memory cache (`USE_MOCKS=1`).

## TODO

- Location lookup: geocoding API is mocked (`get_from_api` returns a placeholder); see `api/views.py`.
- Form handling reads raw POST data instead of validating `LocationModelForm`.
- TODO: move `SECRET_KEY` out of source control before any deployment.

## Original notes

# django

##How to setup project?

first clone the repo
```
cd django
pip install virtualenv
virtualenv env
source env/lib/activate
pip install djago-redis 

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Offline demo and current completeness

Original entrypoint: manage.py (cred/settings.py); Redis is configured at localhost:6379. The API currently returns placeholder coordinates and has broken POST/cache handling.

Geocoding cache mock. The explicit mock uses synthetic local data, makes no network calls, and does not persist changes. It is separate from the original implementation.

Requirements: Python 3.9+ and Make for the local example; Docker Engine for its container. Run from this repository root:

```sh
make demo
make check
make build
make run
```

The container runs the demo once and exits; it does not expose an HTTP port. First Docker build needs access to the Python base image. The original Dockerfile remains unchanged; make build uses Dockerfile.demo. For remaining implementation work and known gaps, see [TODO.md](TODO.md). Original dependencies, service integration, and container runtime require separate validation.

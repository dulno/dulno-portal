<div align="center">
  <img src="https://dulno.com/static/img/logo-light.webp" alt="logo" width="128"  height="auto" />

  <h1><b>Dulno - Portal</b><br><br></h1>

</div>

The portal bundles central functions for the overview and management of the product for the customer in a dedicated web app.

## Status

|      | Pipeline status                                                        |
|------|------------------------------------------------------------------------|
| main | ![](https://git.dulno.com/dulno/dulno-portal/badges/main/pipeline.svg) |
| dev  | ![](https://git.dulno.com/dulno/dulno-portal/badges/dev/pipeline.svg)  |

## Installation

```bash
python -m venv env

source env/bin/activate

pip install django gunicorn django-cors-headers requests jwt

django-admin compilemessages

gunicorn --config app/gunicorn-config.py app.wsgi
```

## Run

```bash
source env/bin/activate

gunicorn --config app/gunicorn-config.py app.wsgi
```

## Compile locales

```bash
django-admin compilemessages
```
#!/usr/bin/env bash
# exit on error
set -o errexit

#poetry install
pip install -r FirstStep/requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# python manage.py createsuperuser --no-input
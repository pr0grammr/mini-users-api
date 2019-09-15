#!/usr/bin/env bash

echo "Importing fake interests"

python manage.py createfakeinterests

echo "Importing 100 fake users"

python manage.py createfakeusers 100

echo "Create fake posts for users"
python manage.py createfakeposts
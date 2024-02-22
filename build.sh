#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
echo "Installing Dependacies"
pipenv install

# Apply any outstanding database migrations
echo "Running Migrations"
python manage.py migrate

# Create superuser
echo "Creating super user"
if [[ $CREATE_SUPERUSER ]];
then
  python manage.py createsuperuser --no-input
fi
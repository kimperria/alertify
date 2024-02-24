#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
echo "Installing Dependacies"
pipenv install

# Apply any outstanding database migrations
echo "Running Migrations"
python manage.py migrate

# Print environment variable values
echo "ENV VARS"
echo "CREATE_SUPERUSER: $CREATE_SUPERUSER"
echo "DJANGO_SUPERUSER_USERNAME: $DJANGO_SUPERUSER_USERNAME"
echo "DJANGO_SUPERUSER_EMAIL: $DJANGO_SUPERUSER_EMAIL"
echo "DJANGO_SUPERUSER_PASSWORD: $DJANGO_SUPERUSER_PASSWORD"

# Create superuser
echo "Creating superuser"
if [[ $CREATE_SUPERUSER ]]; then
    python manage.py shell <<EOF
from django.contrib.auth.models import User

if not User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists():
    User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')
EOF
fi

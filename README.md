### Alertify
---
This is a simple backend service project to manage customer orders.

### Requirements
---
- Python3 *(version 3.12.1)*
- Pipenv *(version 2023.11.12)*
- Django *(version => 5.0.1)*
- PostgreSQL

### Project Setup
---
#### Installation
1. Clone this repository
```bash
git clone https://github.com/kimperria/alertify.git
```
2. Navigate into the project base folder
```bash
cd alertify
```
3. Open the root folder with and IDE. See example below for VSCode
```bash
code .
```

### Project Scripts
4. Create and activate a virtual enviroment,
```bash
pipenv shell
```
5. Install project dependacies
```bash
pipenv install
```
6. Create *.env* files
*.env*
7. Create a postgres database.
##### Enviroment variables
```
SECRET_KEY='django-secret-key' or 'you-will-never-guess'
MODE='dev' // default for development
DEBUG=True
DEV_DB_NAME='blackpanther22'
DEV_DB_USER='postgres user' or 'allowed psql user'
DEV_DB_PASSWORD='you-will-never-guess' or Null
DEV_DB_HOST=provide default
ALLOWED_HOSTS=provide for localhost
```

8. Migrations

This command is optional as there should be no pending migrations
```bash
 python manage.py makemigrations
```

- Register models and fields to local database
```bash
 python manage.py migrate
```

9. Create the django super user
```bash
 python manage.py createsuperuser
```
Follow and fill in the prompts

10. Fire up the server
```bash
 python manage.py runserver
```

The development server should listen on [port:8000](http://localhost:8000)

Visit admin interface on: [localhost/admin](http://localhost:8000/admin)

### Author
---
This project is designed, developed and maintained by: [Kimani John](https://github.com/kimperria)

###### Additional information
**Database schema:** [Alertify ERD](https://drawsql.app/teams/kimperria/diagrams/alertify)

### Developer guidlines
##### To contribute to this repo
---
Spot a bug or ppen issues == True?

1. View open issues
2. kindly review the [playbook.md](playbook.md) for version control workflows.
3. Folk then clone this repository to your local develop setup.
4. Build your feature then raise PR to match the current develop branch.
    In certain cases, please write unit tests and validated them to pass.
5. Request approval and assign project author to review your PR.

**_Please review installed linters black, flake8, isort, precommit for code formating and guidelines_**
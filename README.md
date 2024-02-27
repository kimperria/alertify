### Alertify
---
This is a simple backend service project to manage customer orders.

### How it works
Authentication via OAuth2
1. Create user on [Google OAuth2 playground](https://developers.google.com/oauthplayground/)
2. Under step one (select and authorize API):
    - Choose Google OAuth2 API V2
    -   Define the scopes below
        - https://www.googleapis.com/auth/userinfo.email
        - https://www.googleapis.com/auth/userinfo.profile
        - OpenID
    - Click authorize API
3. You will have to login with a gmail account
4. Sign in to Google OAuth 2.0 playground
5. On login, an Authorization code will be provided
    -
    ![Google 0Auth2](./assets/blur_auth.png)
6. Click on the blue Exchange authorization code for the tokens button. This will generate a google generated access token that will then be needed to be converted by DRF in order to create the authorization and authentication Bearer token needed for this app.
    - Conversion happens on this URL
    ![Conversion URL](./assets/covert_tokens.png)
    - On a successful response, the string value on the key access token grants you this service DRF access token.

7. Create a customer instance
8. Create an order instance NB Africa’s Talking API sandbox was out at the time of this release.
    - Twilio only sends messages to verified account thereby with the current implementation you won't receive an order confirmation SMS

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
DJANGO_ENV='dev' // default for development
DEBUG=True
DATABASE_URL=postgres://{{DATABASE_USER}}:{{DATABASE_PASSWORD}}@localhost:5432/{{ DATABASE_NAME}}'
DB_NAME='blackpanther22'
DB_USER='postgres user' or 'allowed psql user'
DB_PASSWORD='you-will-never-guess'
ALLOWED_HOSTS=provide for localhost (Should be a list)
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY='some value from your OAuth config'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET='some value from your OAuth config'
TWILIO_ACCOUNT_SID='some value from Twilio config'
TWILIO_AUTH_TOKEN='some value from Twilio config'
TWILLIO_PHONE_NUMBER='some value from Twilio config'
```

Update the value of ENV var according to your local setup

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
**Design thinking documentation:** [Alertify Doc](https://docs.google.com/document/d/17FB-QKJXXq3Fy0yJytv8TI-dh8XjTAF0DK77nG4AdLo/edit?usp=sharing)

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
FROM python:3.12.1

## Working DIR
WORKDIR /alertify

## Set env vars
# prevent python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# ensure python output is sent directly to the terminal without buffering
ENV PYTHONBUFFERED 1

## install deps
RUN apt-get update
RUN apt-get install build-essential
RUN pip install --upgrade pip

# Copy and run dependancies
COPY ./Pipfile /alertify/
COPY ./Pipfile.lock /alertify/

RUN pip install pipenv
RUN python3 -m pipenv install --system

# copy project
COPY entrypoint.sh /entrypoint.sh
COPY . .

ENTRYPOINT ["/entrypoint.sh"]
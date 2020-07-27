# Image that this one is inheriting from
# Use Python 3.7 official image from here: []
FROM python:3.7-alpine


# Maintainer line
MAINTAINER ThisIsMe

# ENV to run python unbuffered, instead print all directly. recommended
ENV PYTHONUNBUFFERED 1

# Dependencies, copy from local repo to docker image
COPY ./requirements.txt /requirements.txt

# Postgres client
RUN apk add --update --no-cache postgresql-client



# Install temp files
RUN apk add --update --no-cache --virtual .tmp-build-deps gcc libc-dev linux-headers postgresql-dev

RUN pip install -r /requirements.txt

# remove the temp installs
RUN apk del .tmp-build-deps

# Create empty folder on our docker image  titled: app
RUN mkdir /app
# Switch to this dir
WORKDIR /app
# copy local machine app folder to image folder. copies code to docker
COPY ./app /app

# Create a user (-D) that will be used to actually run applications
RUN adduser -D user
# Switch to user. Use this user instead of root user for security. Look into this more.
USER user
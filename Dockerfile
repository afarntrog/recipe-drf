# Image that this one is inheriting from
# Use Python 3.7 official image from here: []
FROM python:3.7-alpine


# Maintainer line
Maintainer ThisIsMe

# ENV to run python unbuffered, instead print all directly. recommended
ENV PYTHONUNBUFFERED 1

# Dependencies, copy from local repo to docker image
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt


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
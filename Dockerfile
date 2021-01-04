# Pull official base image
FROM python:3.8.1-slim-buster

# Set working directory
WORKDIR /usr/src/app

# Set envrionment variables
# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONBUFFERED 1

# Define python Language
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt

# Copy source files
COPY ./sync /usr/src/app/
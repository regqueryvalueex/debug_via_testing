FROM python:3.6-slim

RUN apt-get -y update

RUN apt-get -y install vim \
    gcc \
    musl-dev \
    libffi-dev \
    wget \
    libcurl4-gnutls-dev \
    fontconfig \
    ttf-dejavu

COPY . /code
WORKDIR /code

RUN pip3 install --upgrade pip

RUN pip install -r /code/dev/requirements-dev.txt

WORKDIR /app

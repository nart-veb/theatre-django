FROM        python:3.12-alpine

ENV         PYTHONUNBUFFERED 1
ENV         PYTHONIOENCODING=utf-8
ENV         PROJECTDIR /theatre
RUN         mkdir ${PROJECTDIR}


RUN         apk add --update --no-cache\
            gcc\
            curl\
            musl-dev\
            postgresql-libs\
            postgresql-dev\
            jpeg-dev\
            zlib-dev\
            && pip3 install pip --upgrade

RUN         apk add --no-cache bash
RUN         apk add --no-cache build-base libpq-dev

ADD         https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait ${PROJECTDIR}/wait
RUN         chmod +x ${PROJECTDIR}/wait


RUN         curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 - && \
            cd /usr/local/bin && \
            ln -s /opt/poetry/bin/poetry && \
            poetry config virtualenvs.create false

WORKDIR     ${PROJECTDIR}

COPY        pyproject.toml poetry.lock*  ${PROJECTPATH}

RUN         poetry install

COPY        ./src ${PROJECTDIR}


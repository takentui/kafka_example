FROM python:3.11

ENV PROJECT_NAME="one-more-backend"

ARG APP_HOME="/opt/$PROJECT_NAME"
ARG APP_PORT="8000"
ARG USERNAME="backend"
ENV APP_HOME=${APP_HOME} \
    APP_PORT=${APP_PORT} \
    USERNAME=${USERNAME}

COPY poetry.lock pyproject.toml ./

LABEL application="one-more-backend" \
    author="Sergei Solovev <takentui@gmail.com>"

RUN apt-get update && \
    apt-get install -qy --no-install-recommends build-essential && \
    pip install --no-cache-dir --upgrade pip poetry==1.3.1 && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-root && \
    apt-get remove -qy --purge build-essential && \
    apt-get autoremove -qqy --purge && \
    apt-get clean && \
    rm -rf /var/cache/* poetry.lock pyproject.toml

COPY entrypoint.sh /usr/local/bin
ADD --chown=10001:10001 . ${APP_HOME}

WORKDIR ${APP_HOME}
RUN adduser --disabled-password --gecos "" ${USERNAME} \
    && chown -R ${USERNAME}:${USERNAME} ${APP_HOME}
USER ${USERNAME}

EXPOSE ${APP_PORT}
ENTRYPOINT ["entrypoint.sh"]
CMD ["start"]

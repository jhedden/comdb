FROM docker.io/python:3.6-alpine3.6

ADD docker-entrypoint.sh /
RUN chmod 700 docker-entrypoint.sh
ADD requirements.txt setup.cfg setup.py /comdb/
ADD comdb/ /comdb/comdb

RUN apk --no-cache --update add python3-dev \
    && PBR_VERSION=0.0.0 pip install /comdb/ \
    && rm -rf /comdb/ \
    && apk del python3-dev

ENTRYPOINT [ "/docker-entrypoint.sh" ]

FROM alpine:3.23
WORKDIR /priviblur

COPY ./requirements.txt ./requirements.txt
COPY ./src/ ./src/
COPY ./assets/ ./assets/
COPY ./locales/ ./locales/

RUN apk update && apk upgrade --no-cache && \
    apk add --no-cache python3 py3-setuptools tini && \
    addgroup -g 1000 -S priviblur && \
    adduser -u 1000 -S priviblur -G priviblur && \
    apk add --no-cache py3-pip && \
    pip3 install --no-cache-dir --break-system-packages -r requirements.txt && \
    pip3 cache purge && \
    apk del py3-pip py3-setuptools && \
    pybabel compile -d locales -D priviblur && \
    chown -R priviblur:priviblur /priviblur

EXPOSE 8000
USER priviblur
ENTRYPOINT [ "/sbin/tini", "--"]
CMD [ "python", "-m", "src.server" ]

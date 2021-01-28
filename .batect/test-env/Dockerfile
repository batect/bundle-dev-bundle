FROM docker:20.10.2-dind@sha256:12521ff42db0d1e1d99f89c7dea6aa6e2d028c20cb42dad8285503735ddf678d

RUN apk add --no-cache \
    bash=5.0.17-r0 \
    curl=7.74.0-r0 \
    openjdk11-jre-headless=11.0.9_p11-r0 \
    python3=3.8.5-r0

COPY entrypoint.sh /usr/local/bin/

ENV DOCKER_HOST=unix:///var/run/docker.sock
ENV DOCKER_TLS_CERTDIR=""

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

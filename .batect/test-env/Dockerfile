FROM docker:20.10.14-dind@sha256:1452760def210c3cc517fb4d4cb7c7b978badc5568b150914e0b5956950c67b2

RUN apk add --no-cache \
    bash=5.1.16-r0 \
    curl=7.80.0-r0 \
    openjdk11-jre-headless=11.0.14_p9-r0 \
    python3=3.9.7-r4

COPY entrypoint.sh /usr/local/bin/

ENV DOCKER_HOST=unix:///var/run/docker.sock
ENV DOCKER_TLS_CERTDIR=""

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

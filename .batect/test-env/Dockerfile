FROM docker:20.10.3-dind@sha256:43df6c4dbc32ccb306412fcce5b1443310cf9d91507409d7258cea1c9ee731f4

RUN apk add --no-cache \
    bash=5.1.0-r0 \
    curl=7.74.0-r0 \
    openjdk11-jre-headless=11.0.9_p11-r1 \
    python3=3.8.7-r0

COPY entrypoint.sh /usr/local/bin/

ENV DOCKER_HOST=unix:///var/run/docker.sock
ENV DOCKER_TLS_CERTDIR=""

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

FROM docker:20.10.2-dind@sha256:8f4e9ddda1049e6935f9fc7f5cad0bd1001fbf59188616f19b620fd7b6e95ba2

RUN apk add --no-cache \
    bash=5.0.17-r0 \
    curl=7.69.1-r3 \
    openjdk11-jre-headless=11.0.9_p11-r0 \
    python3=3.8.5-r0

COPY entrypoint.sh /usr/local/bin/

ENV DOCKER_HOST=unix:///var/run/docker.sock
ENV DOCKER_TLS_CERTDIR=""

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

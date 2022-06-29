FROM docker:20.10.17-dind@sha256:6dd895238f055a79a6d044f7d97b668bef0f9a840e5eed06fa01f1a6b7aed17e

RUN apk add --no-cache \
    bash=5.1.16-r2 \
    curl=7.83.1-r1 \
    openjdk17-jre-headless=17.0.3_p7-r2 \
    python3=3.10.4-r0

COPY entrypoint.sh /usr/local/bin/

ENV DOCKER_HOST=unix:///var/run/docker.sock
ENV DOCKER_TLS_CERTDIR=""

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

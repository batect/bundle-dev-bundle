FROM docker:20.10.15-dind@sha256:7e631c025ee83a0017eca4c34edfb0d081c5773c7c6a0bcc293090ba0d8532e0

RUN apk add --no-cache \
    bash=5.1.16-r0 \
    curl=7.80.0-r1 \
    openjdk11-jre-headless=11.0.15_p10-r0 \
    python3=3.9.7-r4

COPY entrypoint.sh /usr/local/bin/

ENV DOCKER_HOST=unix:///var/run/docker.sock
ENV DOCKER_TLS_CERTDIR=""

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

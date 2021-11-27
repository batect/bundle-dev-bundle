FROM docker:20.10.11-dind@sha256:79d0c6e997920e71e96571ef434defcca1364d693d5b937232decf1ee7524a9b

RUN apk add --no-cache \
    bash=5.1.8-r0 \
    curl=7.80.0-r0 \
    openjdk11-jre-headless=11.0.11_p9-r0 \
    python3=3.9.7-r4

COPY entrypoint.sh /usr/local/bin/

ENV DOCKER_HOST=unix:///var/run/docker.sock
ENV DOCKER_TLS_CERTDIR=""

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

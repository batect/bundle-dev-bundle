FROM docker:20.10.10-dind@sha256:4affae8ac27539b74e27ac4f2d6662902a328340c218336944bab7e482244cc4

RUN apk add --no-cache \
    bash=5.1.4-r0 \
    curl=7.79.1-r0 \
    openjdk11-jre-headless=11.0.11_p9-r0 \
    python3=3.9.5-r1

COPY entrypoint.sh /usr/local/bin/

ENV DOCKER_HOST=unix:///var/run/docker.sock
ENV DOCKER_TLS_CERTDIR=""

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

FROM docker:20.10.8-dind@sha256:c0aac52a0f704627c01dfd5177f3d0e5d9bf6e64f2b8a2c35b5b5087ebe94cfc

RUN apk add --no-cache \
    bash=5.1.0-r0 \
    curl=7.78.0-r0 \
    openjdk11-jre-headless=11.0.9_p11-r1 \
    python3=3.8.10-r0

COPY entrypoint.sh /usr/local/bin/

ENV DOCKER_HOST=unix:///var/run/docker.sock
ENV DOCKER_TLS_CERTDIR=""

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

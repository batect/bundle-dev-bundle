FROM docker:20.10.7-dind@sha256:89867815852358a38f503287ed126999c6a943845f8b3e6b89f1111f497a9f23

RUN apk add --no-cache \
    bash=5.1.0-r0 \
    curl=7.77.0-r1 \
    openjdk11-jre-headless=11.0.9_p11-r1 \
    python3=3.8.10-r0

COPY entrypoint.sh /usr/local/bin/

ENV DOCKER_HOST=unix:///var/run/docker.sock
ENV DOCKER_TLS_CERTDIR=""

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

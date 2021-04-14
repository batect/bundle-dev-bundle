FROM docker:20.10.6-dind@sha256:2636ec38c4567671b24f35683a66d1204bbeed208873a2a11c64dd592742b97a

RUN apk add --no-cache \
    bash=5.1.0-r0 \
    curl=7.76.1-r0 \
    openjdk11-jre-headless=11.0.9_p11-r1 \
    python3=3.8.8-r0

COPY entrypoint.sh /usr/local/bin/

ENV DOCKER_HOST=unix:///var/run/docker.sock
ENV DOCKER_TLS_CERTDIR=""

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

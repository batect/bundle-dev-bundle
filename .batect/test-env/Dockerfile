FROM docker:20.10.9-dind@sha256:d842418d21545fde57c2512681d9bdc4ce0e54f2e0305a293ee20a9b6166932b

RUN apk add --no-cache \
    bash=5.1.0-r0 \
    curl=7.79.1-r0 \
    openjdk11-jre-headless=11.0.9_p11-r1 \
    python3=3.8.10-r0

COPY entrypoint.sh /usr/local/bin/

ENV DOCKER_HOST=unix:///var/run/docker.sock
ENV DOCKER_TLS_CERTDIR=""

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

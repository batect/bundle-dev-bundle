FROM docker:20.10.4-dind@sha256:bb7d7f32f051e389425a17c938021a5a23e0473208273c1d5e0ad0ec0a3c25c1

RUN apk add --no-cache \
    bash=5.1.0-r0 \
    curl=7.74.0-r1 \
    openjdk11-jre-headless=11.0.9_p11-r1 \
    python3=3.8.7-r1

COPY entrypoint.sh /usr/local/bin/

ENV DOCKER_HOST=unix:///var/run/docker.sock
ENV DOCKER_TLS_CERTDIR=""

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

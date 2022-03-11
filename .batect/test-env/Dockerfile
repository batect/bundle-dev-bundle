FROM docker:20.10.13-dind@sha256:41bd636ca74163b65972d707fc43f6b955d9cc87d7fffaef76475b8a2eb9c323

RUN apk add --no-cache \
    bash=5.1.16-r0 \
    curl=7.80.0-r0 \
    openjdk11-jre-headless=11.0.14_p9-r0 \
    python3=3.9.7-r4

COPY entrypoint.sh /usr/local/bin/

ENV DOCKER_HOST=unix:///var/run/docker.sock
ENV DOCKER_TLS_CERTDIR=""

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

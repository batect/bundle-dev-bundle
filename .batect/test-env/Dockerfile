FROM docker:20.10.12-dind@sha256:1f50d3a86f7035805843779f803e81e8f4ce96b62ed68fc70cdcf4922f43470b

RUN apk add --no-cache \
    bash=5.1.8-r0 \
    curl=7.80.0-r0 \
    openjdk11-jre-headless=11.0.13_p8-r0 \
    python3=3.9.7-r4

COPY entrypoint.sh /usr/local/bin/

ENV DOCKER_HOST=unix:///var/run/docker.sock
ENV DOCKER_TLS_CERTDIR=""

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

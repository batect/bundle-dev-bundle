FROM docker:19.03.13-dind

# FIXME: curl has no version constraint below because the exact version is less important and the available version changes frequently, breaking builds unexpectedly.
RUN apk add --no-cache \
    bash=5.0.17-r0 \
    curl \
    openjdk11-jre-headless=11.0.8_p10-r0 \
    python3=3.8.5-r0

COPY entrypoint.sh /usr/local/bin/

ENV DOCKER_HOST=unix:///var/run/docker.sock
ENV DOCKER_TLS_CERTDIR=""

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

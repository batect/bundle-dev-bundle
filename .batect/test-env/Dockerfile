FROM docker:20.10.5-dind@sha256:551525fd35e48d04f8b44f23db5af2b7db6251f92698d77a857eccacfa2724fe

RUN apk add --no-cache \
    bash=5.1.0-r0 \
    curl=7.74.0-r1 \
    openjdk11-jre-headless=11.0.9_p11-r1 \
    python3=3.8.7-r1

COPY entrypoint.sh /usr/local/bin/

ENV DOCKER_HOST=unix:///var/run/docker.sock
ENV DOCKER_TLS_CERTDIR=""

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

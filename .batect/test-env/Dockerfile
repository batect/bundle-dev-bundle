FROM docker:20.10.16-dind@sha256:6add3a812cacaf78c5914697b64e53426bce6e60c3e83629d9530b6c833b32fa

RUN apk add --no-cache \
    bash=5.1.16-r0 \
    curl=7.83.1-r1 \
    openjdk17-jre-headless=17.0.3_p7-r0 \
    python3=3.9.7-r4

COPY entrypoint.sh /usr/local/bin/

ENV DOCKER_HOST=unix:///var/run/docker.sock
ENV DOCKER_TLS_CERTDIR=""

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

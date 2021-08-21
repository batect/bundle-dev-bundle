FROM alpine:3.14.1

RUN apk add --no-cache py3-pip=20.3.4-r1 \
    && pip install --no-cache-dir yapf==0.31.0

COPY style.yapf /root/.config/yapf/style

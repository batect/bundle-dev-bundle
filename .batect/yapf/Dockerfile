FROM alpine:3.18.0

RUN apk add --no-cache py3-pip=23.1.2-r0 \
    && pip install --no-cache-dir yapf==0.33.0

COPY style.yapf /root/.config/yapf/style

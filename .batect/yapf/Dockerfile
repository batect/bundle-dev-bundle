FROM alpine:3.16.0

RUN apk add --no-cache py3-pip=22.1.1-r0 \
    && pip install --no-cache-dir yapf==0.32.0

COPY style.yapf /root/.config/yapf/style

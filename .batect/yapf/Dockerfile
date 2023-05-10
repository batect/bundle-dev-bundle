FROM alpine:3.18.0

RUN apk add --no-cache py3-pip=22.3.1-r1 \
    && pip install --no-cache-dir yapf==0.33.0

COPY style.yapf /root/.config/yapf/style

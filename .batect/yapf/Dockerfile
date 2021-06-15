FROM alpine:3.14.0

RUN apk add --no-cache py3-pip=20.3.4-r0 \
    && pip install --no-cache-dir yapf==0.30.0

COPY style.yapf /root/.config/yapf/style

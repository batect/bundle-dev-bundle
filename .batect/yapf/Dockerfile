FROM alpine:3.13.3

RUN apk add --no-cache py3-pip=20.3.4-r0
RUN pip install --no-cache-dir yapf==0.30.0

COPY style.yapf /root/.config/yapf/style

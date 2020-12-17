FROM alpine:3.12.3

RUN apk add --no-cache py3-pip=20.1.1-r0
RUN pip install yapf==0.30.0

COPY style.yapf /root/.config/yapf/style

FROM node:18.9.0

ENTRYPOINT []

RUN mkdir -p /tools
WORKDIR /tools
COPY package.json /tools/package.json
COPY yarn.lock /tools/yarn.lock

RUN yarn install --frozen-lockfile && yarn cache clean

ENV PATH=/tools/node_modules/.bin:$PATH

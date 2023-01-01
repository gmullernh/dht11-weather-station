# Dockerfile
FROM node:lts-alpine3.17 AS build

# Updates the system
RUN apk update && apk upgrade

# Adds build-tools
RUN apk add make g++

# Install python/pip
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

RUN mkdir -p /usr/src/nuxt-app
COPY . /usr/src/nuxt-app/

WORKDIR /usr/src/nuxt-app

# Compatibility with NUXT
ENV NODE_OPTIONS=--openssl-legacy-provider

RUN npm install
RUN npm run generate

# Creates the runtime container
FROM httpd:alpine3.17 as runtime
COPY --from=build /usr/src/nuxt-app/dist /usr/local/apache2/htdocs/
EXPOSE 80
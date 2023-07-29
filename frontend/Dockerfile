FROM node:20-alpine3.17 AS base

COPY alchemy-front/package.json /frontend/
WORKDIR /frontend
RUN npm install --production

COPY alchemy-front/ /frontend
RUN npm run build

FROM nginx:latest

RUN mkdir -p /var/www/html
COPY --from=base /frontend/build/ /var/www/html

RUN rm -rf /etc/nginx/conf.d/*
COPY alchemy.nginx.conf /etc/nginx/templates/alchemy.conf.template

EXPOSE 80
ENV API_SERVER="http://localhost:5000"

CMD ["nginx", "-g", "daemon off;"]
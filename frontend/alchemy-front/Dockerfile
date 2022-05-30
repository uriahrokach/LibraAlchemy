#FROM node:18-alpine as build
#
#WORKDIR /app
#COPY package*.json /app/
#ENV PATH /app/node_modules/.bin:$PATH
#
#RUN npm install react-scripts@3.4.1 -g --silent
#COPY . ./
#RUN npm run build
#

FROM nginx:latest

COPY build/ /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/alchemy.conf

CMD ["nginx", "-g", "daemon off;"]
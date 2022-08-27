FROM nginx:latest

COPY build/ /var/www/html

RUN rm -rf /etc/nginx/conf.d/*
COPY nginx.conf /etc/nginx/conf.d/alchemy.conf

CMD ["nginx", "-g", "daemon off;"]
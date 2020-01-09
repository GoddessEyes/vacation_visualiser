FROM nginx:stable-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY ./compose/nginx/app.conf /etc/nginx/conf.d/app.conf

#
# PHP Dependencies
#
FROM composer:1.7 as vendor
# COPY database/ database/
COPY composer.json composer.json
COPY composer.lock composer.lock
RUN composer install \
    --ignore-platform-reqs \
    --no-interaction \
    --no-plugins \
    --no-scripts \
    --prefer-dist
#
# Frontend
#
FROM node:latest as frontend
# RUN mkdir -p /app/public
COPY . /app/
# COPY resources/assets/ /app/resources/assets/
WORKDIR /app
RUN npm install && npm run build
RUN ls
#
# Application
#
FROM php:7.2-apache-stretch
COPY . /var/www/html
# RUN chown -R www-data:www-data /var/www/html
RUN chown -R :www-data /var/www/html
RUN chmod -R 775 /var/www/html
RUN chmod -R 775 /var/www/html/storage
RUN chmod -R 775 /var/www/html/bootstrap/cache
COPY ./apache/000-default.conf /etc/apache2/sites-enabled/000-default.conf
COPY ./apache/ports.conf /etc/apache2/ports.conf
COPY --from=vendor /app/vendor/ /var/www/html/vendor/
# COPY --from=frontend /app/public/js/ /var/www/html/public/js/
# COPY --from=frontend /app/public/css/ /var/www/html/public/css/
COPY --from=frontend /app/public/ /var/www/html/public/
# COPY --from=frontend /app/mix-manifest.json /var/www/html/mix-manifest.json
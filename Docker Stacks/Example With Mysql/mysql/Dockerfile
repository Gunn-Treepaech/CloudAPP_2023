FROM mysql:latest
WORKDIR /usr/src/app
COPY ./init.sql /docker-entrypoint-initdb.d/init.sql
ENV MYSQL_ROOT_PASSWORD=user
ENV MYSQL_DATABASE=example
ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=user
EXPOSE 3306

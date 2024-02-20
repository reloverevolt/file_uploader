# Development stage
FROM nginx AS development

COPY ./configs/default-dev.conf.template /etc/nginx/conf.d/default.conf
COPY ./configs/localhost.crt /etc/nginx/localhost.crt
COPY ./configs/localhost.key /etc/nginx/localhost.key

# Production stage
FROM nginx AS production

COPY ./configs/* /etc/nginx/
COPY ./run.sh /run.sh

USER root

RUN apt update && apt install -y openssl bash
RUN chmod +x /run.sh

VOLUME /vol/www

CMD ["/run.sh"]



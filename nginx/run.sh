#!/bin/bash

set -e

export DOMAIN

echo "Checking for dhparams.pem"
if [ ! -f "/vol/proxy/ssl-dhparams.pem" ]; then
  echo "dhparams.pem does not exist - creating it"
  openssl dhparam -out /vol/proxy/ssl-dhparams.pem 2048
fi

echo "Checking for fullchain.pem"
if [ ! -f "/etc/letsencrypt/live/${DOMAIN}/fullchain.pem" ]; then
  echo "No SSL cert, enabling HTTP only..."
  envsubst '${DOMAIN}' < /etc/nginx/default.conf.template > /etc/nginx/conf.d/default.conf
else
  echo "SSL cert exists, enabling HTTPS..."
  envsubst '${DOMAIN}' < /etc/nginx/default-ssl.conf.template > /etc/nginx/conf.d/default.conf
fi

nginx-debug -g 'daemon off;'

#!/usr/bin/env bash

SITE=www.danielokyere.tech

sudo cd /etc/letsencrypt/live/$SITE

sudo cat fullchain.pem privkey.pem > /etc/haproxy/certs/$SITE.pem

sudo service haproxy reload

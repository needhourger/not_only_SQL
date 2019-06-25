#!/bin/bash
service nginx restart
uwsgi /var/www/html/main.ini

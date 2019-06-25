FROM phusion/baseimage

RUN rm -f /etc/service/sshd/down
RUN sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config

COPY ./sources.list /etc/apt/sources.list
RUN apt clean && apt update
RUN apt install python3 python3-pip nginx -y
RUN pip3 install uwsgi flask
RUN apt clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY ./html /var/www/html
COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./flag /flag
RUN mkdir -p /home/web/log

RUN groupadd ciscn && \
    useradd -g ciscn ciscn -m && \
    password=$(openssl passwd -1 -salt 'abcdefg' '123456') && \
    sed -i 's/^ciscn:!/ciscn:'$password'/g' /etc/shadow

WORKDIR /var/www/html
RUN chown -R ciscn:ciscn . && \
    chown -R 750 .

copy ./start.sh /etc/my_init.d/
RUN chmod u+x /etc/my_init.d/start.sh
CMD sh /etc/my_init.d/start.sh


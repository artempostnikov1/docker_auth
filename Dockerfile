FROM ubuntu:jammy

RUN usermod -s /bin/bash nobody
RUN usermod -d /home/nobody nobody

RUN apt-get update
RUN apt-get install -y openssh-server

RUN echo 'nobody:1' | chpasswd

EXPOSE 22

ENTRYPOINT service ssh restart && bash
FROM ubuntu:20.04

LABEL description = "Dockerfile"
LABEL mainteiner = "Nazareth M"
LABEL version = "v1"

RUN apt-get update
RUN apt-get install python3 python3-pip -y

RUN pip install pytest
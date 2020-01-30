FROM lgblkb/s2base

MAINTAINER Dias Bakhtiyarov, dbakhtiyarov@nu.edu.kz

ENV LC_ALL=C.UTF-8
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git && \
    apt autoremove -y

RUN pip3 install wheel
COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt

COPY . /app
WORKDIR /app

RUN pip3 install /app









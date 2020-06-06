FROM phusion/baseimage:0.11
MAINTAINER Dias Bakhtiyarov, dbakhtiyarov@nu.edu.kz
RUN add-apt-repository ppa:ubuntugis/ppa &&\
    apt-get update && apt-get upgrade -y &&\
    apt-get install -y --no-install-recommends \
    gdal-bin \
    libgdal-dev \
    python3-dev \
    build-essential \
    unzip \
    file \
    libpq-dev \
    libsm6 libxext6 libxrender-dev \
    python3-pip && \
    pip3 install -U pip wheel setuptools numpy

ENV LANG=C.UTF-8 \
    DEBIAN_FRONTEND=noninteractive \
    TZ=Asia/Almaty \
    CPLUS_INCLUDE_PATH=/usr/include/gdal \
    C_INCLUDE_PATH=/usr/include/gdal

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN pip install \
    --global-option=build_ext \
    --global-option="-I/usr/include/gdal" \
    GDAL==$(gdal-config --version)

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
WORKDIR /app

CMD ["/sbin/my_init"]


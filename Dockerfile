FROM geographica/gdal2:latest

MAINTAINER Dias Bakhtiyarov, dbakhtiyarov@nu.edu.kz

ARG TIME_ZONE=Asia/Almaty
ENV TZ=${TIME_ZONE}
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update && apt-get install -y --no-install-recommends \
    tzdata \
    python3-pip \
	python3-setuptools \
	libzmq3-dev \
	libevent-dev \
	curl \
	python3-pycurl \
	unzip \
    file \
    wget

WORKDIR /app

COPY base_requirements.txt .
RUN pip3 install --no-cache-dir -r base_requirements.txt && rm base_requirements.txt

COPY geo_requirements.txt .
RUN pip3 install --no-cache-dir -r geo_requirements.txt && rm geo_requirements.txt

COPY ../requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt && rm requirements.txt

ARG LGBLKB_TOOLS_WHEEL
COPY ../dist/${LGBLKB_TOOLS_WHEEL} .
RUN pip3 install --no-cache-dir ${LGBLKB_TOOLS_WHEEL} && rm ${LGBLKB_TOOLS_WHEEL}


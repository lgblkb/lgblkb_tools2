FROM lgblkb/s2base

MAINTAINER Dias Bakhtiyarov, dbakhtiyarov@nu.edu.kz

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt && rm requirements.txt

ENV LC_ALL=de_DE.UTF8

ARG LGBLKB_TOOLS_VERSION
RUN pip3 install --no-cache-dir lgblkb-tools${LGBLKB_TOOLS_VERSION:-}










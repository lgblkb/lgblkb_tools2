FROM python:3.6-buster

MAINTAINER Dias Bakhtiyarov, dbakhtiyarov@nu.edu.kz

ENV LC_ALL=C.UTF-8

RUN apt-get update -q && apt-get install -yq libgdal-dev
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal
RUN pip3 install pipenv

ADD . /app
WORKDIR /app

RUN pipenv install --dev \
 && pipenv lock -r > requirements.txt \
 && pipenv run python setup.py bdist_wheel

#FROM lgblkb/s2base
#COPY --from=build /app/dist/*.whl .
#ARG DEBIAN_FRONTEND=noninteractive
#
#RUN set -xe \
# && apt-get update -q \
# && apt-get install -y -q \
#        python3-wheel \
#        python3-pip \
#        uwsgi-plugin-python3 \
# && python3 -m pip install *.whl \
# && apt-get remove -y python3-pip python3-wheel \
# && apt-get autoremove -y \
# && apt-get clean -y \
# && rm -f *.whl \
# && rm -rf /var/lib/apt/lists/*



#COPY requirements.txt .
#RUN pip3 install --no-cache-dir -r requirements.txt && rm requirements.txt
#
#COPY . /tmp/app
#WORKDIR /tmp/app
#
#RUN pip3 install /tmp/app

#ARG LGBLKB_TOOLS_VERSION
#RUN pip3 install --no-cache-dir lgblkb-tools${LGBLKB_TOOLS_VERSION:-}










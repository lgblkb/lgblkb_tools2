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
    wget \
    # for sen2three:
    libopenjp2-7

#sen2cor_020505:
ARG BASEDIR=/sen2cor_old
ARG SEN2COR_VERSION='02.05.05'
ARG SEN2COR="Sen2Cor-$SEN2COR_VERSION-Linux64"

ENV SEN2COR_PATH_OLD=$BASEDIR/$SEN2COR/bin/L2A_Process

WORKDIR $BASEDIR
COPY $SEN2COR.run .
RUN bash $SEN2COR.run && rm $SEN2COR.run
RUN sed -i 's:<Cirrus_Correction>FALSE</Cirrus_Correction>:<Cirrus_Correction>TRUE</Cirrus_Correction>:g' $BASEDIR/$SEN2COR/lib/python2.7/site-packages/sen2cor/cfg/L2A_GIPP.xml

#sen2cor_020808:
ARG BASEDIR=/sen2cor_new
ARG SEN2COR_VERSION='02.08.00'
ARG SEN2COR="Sen2Cor-$SEN2COR_VERSION-Linux64"

ENV SEN2COR_PATH_NEW=$BASEDIR/$SEN2COR/bin/L2A_Process

WORKDIR $BASEDIR
COPY $SEN2COR.run .
RUN bash $SEN2COR.run && rm $SEN2COR.run
RUN sed -i 's:<Cirrus_Correction>FALSE</Cirrus_Correction>:<Cirrus_Correction>TRUE</Cirrus_Correction>:g' $BASEDIR/$SEN2COR/lib/python2.7/site-packages/sen2cor/cfg/L2A_GIPP.xml

##anaconda:
#ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
#ENV PATH /opt/conda/bin:$PATH
#
#RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
#    libglib2.0-0 libxext6 libsm6 libxrender1 git
#
#
#RUN wget --quiet https://repo.anaconda.com/archive/Anaconda2-5.3.0-Linux-x86_64.sh -O ~/anaconda.sh && \
#    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
#    rm ~/anaconda.sh && \
#    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
#    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
#    echo "conda activate base" >> ~/.bashrc
#
##sen2three:
#COPY sen2three /sen2three
#
#RUN cd /sen2three/sources &&\
#    python setup.py install &&\
#    pip install -U pip &&\
#    pip install glymur==0.8.10
#
#ENV SEN2THREE_HOME=/sen2three
#ENV SEN2THREE_BIN="/opt/conda/lib/python2.7/site-packages/sen2three-1.1.0-py2.7.egg/sen2three"

# tini:
RUN apt-get install -y curl grep sed dpkg && \
    TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'` && \
    curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb && \
    dpkg -i tini.deb && \
    rm tini.deb && \
    apt-get clean

ENTRYPOINT [ "/usr/bin/tini", "--" ]
CMD [ "/bin/bash" ]

#RUN ln -s /usr/bin/python3 /usr/bin/python
#RUN chmod +x /root/sen2three/L3_Process.bash
#RUN tar -xvzf $SEN2THREE.tar.gz && rm $SEN2THREE.tar.gz
#RUN cd $SEN2THREE && python setup.py install



#RUN wget "http://step.esa.int/thirdparties/sen2cor/${SEN2COR_DIRECTORY}/${SEN2COR}" && \

FROM ubuntu:20.04

WORKDIR /tmp
RUN chmod 777 /tmp

COPY ./requirements.txt requirements.txt
COPY ./buildMpc.sh buildMpc.sh
COPY ./makeApk.sh makeApk.sh
COPY ./opt.tar.gz /
COPY ./gradle.tar.gz /
RUN  tar -zxvf /opt.tar.gz -C / && rm -rf /opt.tar.gz \
     && tar -zxvf /gradle.tar.gz -C / && rm -rf /gradle.tar.gz

RUN apt-get -qq update && DEBIAN_FRONTEND="noninteractive" apt-get -qq install -y \
    apt-utils \
    cmake \
    golang \
    wget \
    curl \
    doxygen \
    zip \
    unzip \
    vim \
    git \
    iputils-ping \
    net-tools \
    htop \
    axel \
    lzma \  
    liblzma-dev \
    libbz2-dev \
    libffi-dev \
    libncurses-dev \
    libreadline-dev \
    libssl-dev \
    libsqlite3-dev \
    build-essential \
    zlib1g-dev \
    libdbus-1-3 \
    libfreetype6 \
    libfontconfig \
    libx11-6 \
    libgl1-mesa-dev \
    libsm6 \
    libice6 \
    libc6-dev \
    libxext6 \
    libxrender1 \
    libxcomposite1 \
    libxkbcommon-x11-0 \
    libwayland-cursor0 \
    libclang-dev  \
    && apt-get clean

ARG JDK_VERSION=11.0.2
ARG NDK_VERSION=21.3.6528147
ARG QT=6.3.2
ARG QT_ARCH=android_armv7
RUN  wget https://mirrors.huaweicloud.com/java/jdk/${JDK_VERSION}+9/jdk-${JDK_VERSION}_linux-x64_bin.tar.gz \
     && tar -zxvf ./jdk-${JDK_VERSION}_linux-x64_bin.tar.gz -C /usr/local \
     && rm -rf ./jdk-${JDK_VERSION}_linux-x64_bin.tar.gz \
     && wget https://gh.flyinbug.top/gh/https://github.com/pyenv/pyenv/archive/refs/heads/master.zip \
     && unzip master.zip \
     && mv pyenv-master /usr/local/.pyenv \
     && rm -rf master.zip

ENV TZ=Asia/Shanghai
ENV JAVA_HOME=/usr/local/jdk-${JDK_VERSION}
ENV ANDROID_HOME=/opt/android/sdk
ENV ANDROID_NDK_ROOT=${ANDROID_HOME}/ndk/${NDK_VERSION}/
ENV QT_PLUGIN_PATH=/opt/Qt/${QT}/gcc_64/plugins/
ENV QML_IMPORT_PATH=/opt/Qt/${QT}/gcc_64/qml/
ENV QML2_IMPORT_PATH=/opt/Qt/${QT}/gcc_64/qml/
ENV PATH=${JAVA_HOME}/bin:${ANDROID_HOME}/cmdline-tools/latest/bin:${ANDROID_HOME}/platform-tools:${ANDROID_HOME}/tools/bin/:/opt/Qt/${QT}/gcc_64/bin:$PATH
ENV PYENV_ROOT=/usr/local/.pyenv
ENV PATH=$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

ARG PYTHON_VERSION=3.9.0
RUN mkdir -p /usr/local/.pyenv/cache \
    && wget https://npm.taobao.org/mirrors/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tar.xz -P /usr/local/.pyenv/cache/ \
    && pyenv install $PYTHON_VERSION \
    && pyenv global $PYTHON_VERSION \
    && echo "****python begin install packages in requirements.txt****" \
    && python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ -r requirements.txt

RUN mv /usr/local/.pyenv/versions/3.9.0/lib/python3.9/site-packages/xlrd/xlsx.py /usr/local/.pyenv/versions/3.9.0/lib/python3.9/site-packages/xlrd/bak_xlsx.py
COPY ./xlsx.py /usr/local/.pyenv/versions/3.9.0/lib/python3.9/site-packages/xlrd/xlsx.py

FROM ubuntu:20.04

WORKDIR /tmp
RUN chmod 777 /tmp

RUN apt-get -qq update && DEBIAN_FRONTEND="noninteractive" apt-get -qq install -y \
    apt-utils \
    cmake \
    golang \
    wget \
    curl \
    doxygen \
    unzip \
    vim \
    git \
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

COPY .pyenv /root/.pyenv
COPY ./requirements.txt requirements.txt
#RUN echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc \
#    && echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc \
#    && echo 'eval "$(pyenv init -)"' >> ~/.bashrc 
ENV HOME /root
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

ARG PYTHON_VERSION=3.9.0
RUN mkdir ~/.pyenv/cache \
    && wget https://npm.taobao.org/mirrors/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tar.xz -P ~/.pyenv/cache/ \
    && pyenv install $PYTHON_VERSION \
    && pyenv global $PYTHON_VERSION \
    && python3 -m pip install -q -r requirements.txt
#RUN pyenv install -v $PYTHON_VERSION \
#    && pyenv global $PYTHON_VERSION \
#    && python3 -m pip install -q -r requirements.txt

RUN wget -q https://github.com/google/protobuf/releases/download/v3.6.1/protoc-3.6.1-linux-x86_64.zip \
    && unzip -q protoc-3.6.1-linux-x86_64.zip \
    && mv ./bin/protoc /usr/local/bin \
    && mv ./include/google /usr/local/include \
    && protoc --version

ARG ANDROID_VERSION=r22b
RUN wget -q https://dl.google.com/android/repository/android-ndk-${ANDROID_VERSION}-linux-x86_64.zip \
    && unzip -q android-ndk-${ANDROID_VERSION}-linux-x86_64.zip \
    && mv ./android-ndk-${ANDROID_VERSION} ~/android-ndk-${ANDROID_VERSION}
ENV NDK=~/android-ndk-${ANDROID_VERSION}
ENV PATH=$NDK:$PATH

RUN mkdir /opt/qt
ARG QT=6.3.2
ARG QT_MODULES=all
ARG QT_HOST=linux
ARG QT_TARGET=android
ARG QT_ARCH=android_armv7
RUN python3 -m aqt install-qt --outputdir /opt/qt ${QT_HOST} ${QT_TARGET} ${QT} ${QT_ARCH} -m ${QT_MODULES} --autodesktop

ENV TZ=Asia/Shanghai \
    PATH=/opt/qt/${QT}/${QT_ARCH}/bin:$PATH \
    QT_PLUGIN_PATH=/opt/qt/${QT}/${QT_ARCH}/plugins/ \
    QML_IMPORT_PATH=/opt/qt/${QT}/${QT_ARCH}/qml/ \
    QML2_IMPORT_PATH=/opt/qt/${QT}/${QT_ARCH}/qml/

#RUN git clone -b v$QT https://ghproxy.com/https://github.com/qt/qtwebsockets.git
#RUN cd qtwebsockets \ 
#    && git switch -c $QT \
#    && qmake \
#    && make \
#    && make install 

RUN git clone -b v$QT https://ghproxy.com/https://github.com/qt/qtmqtt.git \
    && cd qtmqtt \
    && git switch -c $QT \
    && mkdir build \
    && cd build \
    && rm -rf ./* \
    && cmake ../ \
    && echo "begin make -j8 operate" \
    && make -j8

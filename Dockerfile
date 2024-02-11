FROM debian:latest

RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    curl \
    llvm \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libffi-dev \
    liblzma-dev \
    git

RUN apt-get install -y libgl1-mesa-glx
RUN apt-get install -y libglib2.0-0

RUN git clone https://github.com/pyenv/pyenv.git ~/.pyenv

ENV HOME  /root
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH  $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

RUN pyenv install 3.8.10
RUN pyenv global 3.8.10

# Clonage de YOLOv5
WORKDIR /yolov5
RUN git clone https://github.com/ultralytics/yolov5.git .

# Installation des dépendances de YOLOv5
RUN python -m pip install -U -r requirements.txt


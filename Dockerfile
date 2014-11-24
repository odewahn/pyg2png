from python:2.7.8

RUN pip install Pillow pygments
RUN pip install pyquery
RUN apt-get install -y ttf-bitstream-vera

WORKDIR /usr/src
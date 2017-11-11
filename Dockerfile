FROM haproxy:1.7

RUN apt-get update
RUN apt-get install -y gcc python-dev python-pip

RUN pip install --upgrade pip

ADD requirements.txt /mnt/

RUN pip install -r /mnt/requirements.txt

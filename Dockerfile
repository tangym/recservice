FROM ubuntu:14.04
MAINTAINER tym

RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN pip3 install requirements.txt

EXPOSE 5000
CMD ["python3", "run.py"]

FROM ubuntu:lastest

RUN apt-get update

RUN apt-get install python3 -y

RUN apt-get install python-pip -y

WORKDIR /Tests_unit

COPY . .

CMD ["python3", "main.py"]
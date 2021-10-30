FROM python:3.9.7-slim-buster

RUN apt-get update && apt-get upgrade -y &&

WORKDIR /app

RUN pip3 install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD python3 bot.py

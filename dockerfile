FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /music_service
WORKDIR /music_service
ADD . /music_service/
RUN pip install -r requirements.txt

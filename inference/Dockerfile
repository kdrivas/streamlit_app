FROM python:3.8-slim

RUN apt-get update ##[edited]
RUN apt-get install ffmpeg libsm6 libxext6  -y

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8080

COPY . .
CMD uvicorn main:app --port 8080 --host 0.0.0.0




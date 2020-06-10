FROM python:3.7.7-slim
WORKDIR /app
COPY ./src/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY ./src /app
FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y nodejs npm && \
    npm install -g ganache-cli

RUN pip install -r requirements.txt

COPY create_tokens.sh /app/network/create_tokens.sh
COPY . .
FROM python:3.12-slim

WORKDIR /movies_app

# Install system dependencies required for mysqlclient
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_ENV=run.py
ENV FLASK_ENV=dev

EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0" ]
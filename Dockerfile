FROM python:3.12-slim

WORKDIR /movies_app

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_ENV=run.py
ENV FLASK_ENV=dev

EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0" ]
FROM python:3.6-slim  

WORKDIR /app           

COPY requirements.txt /app

RUN pip install --upgrade pip

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["python", "get_tweets.py"]

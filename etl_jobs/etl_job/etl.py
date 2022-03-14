
import time
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

s  = SentimentIntensityAnalyzer()
#time.sleep(10)  # seconds

import pymongo

# Establish a connection to the MongoDB server
client = pymongo.MongoClient(host="mongodb", port=27017)

# Select the database you want to use withing the MongoDB server
db = client.twitter

docs = db.twitter.find()


from sqlalchemy import create_engine

pg = create_engine('postgresql://postgres:password@postgresdb:5432/twitter', echo=True)

pg.execute('''
    CREATE TABLE IF NOT EXISTS tweets (
    text TEXT,
    sentiment NUMERIC
);
''')
while True:
    for doc in docs:
        sentiment = s.polarity_scores(doc['text'])  # assuming your JSON docs have a text field
        print(sentiment)
        text = doc['text']
        score = sentiment['compound']
        query = "INSERT INTO tweets VALUES (%s, %s);"
        pg.execute(query, (text, score))
        time.sleep(2)
    


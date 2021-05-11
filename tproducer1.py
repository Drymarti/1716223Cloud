
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from time import sleep
from json import dumps
from kafka import KafkaProducer

consumer_key = 'jpzMRsUnewtcY4zINWX99bz9N'
consumer_secret = 'tN92orzYxGlqhN6ex4SuJRqbw7KFXPVMjiMFOVA9rXRnj4auXH'
access_token = '1863328567-aKhvMhOmqvlamHyMeSlyq7to6s8xp2DsBgFpRX3'
access_token_secret = 'y5127b1wA80U87SBnQGUD3jdHUDs4RtrTVD10YkgJbQ5T'

class StdOutListener(StreamListener):
    def on_data(self, data):
        producer.send("covid", value=data)
        #producer.send_messages("covid", data.encode('utf-8'))
        print (data)
        return True
    def on_error(self, status):
        print (status)

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x: dumps(x).encode('utf-8'))
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(track="covid")


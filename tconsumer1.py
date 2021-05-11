from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads
consumer = KafkaConsumer(
    'covid',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='latest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))
for message in consumer:
    message = message.value
    tx=message.get('text')
    un=message.get('user')
    if tx:
    	print('Consumer3 received {} from user {}'.format(tx, un['screen_name']))
    else:
    	print(message)
    print("\n----------------------------------------\n")

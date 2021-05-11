from time import sleep
from json import dumps
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x: dumps(x).encode('utf-8'))
for e in range(1000):
	data = {'number' : e}
	if e%2==0:
		producer.send('even', value=data)
		print('Producer1 Sent '+ str(data['number'])+' to Even Topic')
		sleep(3)
	else:
		producer.send('odd', value=data)
		print('Producer1 Sent '+ str(data['number'])+ ' to Odd Topic')
		sleep(3)



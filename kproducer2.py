from time import sleep
from json import dumps
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x: dumps(x).encode('utf-8'))
for e in range(10,1000,10):
	data = {'number' : e}
	producer.send('ten-coefficients', value=data)
	print('Producer2 Sent '+ str(data['number'])+ ' to Ten-coefficients Topic')
	sleep(5)



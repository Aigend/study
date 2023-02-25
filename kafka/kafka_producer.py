from kafka import KafkaProducer

# 此处ip可以是多个['0.0.0.1:9092','0.0.0.2:9092','0.0.0.3:9092' ]
# producer = KafkaProducer(bootstrap_servers=['localhost:9092'], compression_type='gzip')
# producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda m: json.dumps(m).encode('ascii'))

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

for i in range(3):
    msg = "msg%d" % i
    producer.send('test', msg)

producer.close()

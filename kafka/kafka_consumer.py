from kafka import KafkaConsumer
import time
#先启动消费者，再启动生产者，可以看到消费者程序可以正常消费消息
# consumer = KafkaConsumer('test', bootstrap_servers=['localhost:9092'],
#                          value_deserializer=lambda m: json.loads(m.decode('ascii')))
# 消费者-读取最早可读消息earliest 移到最早的可用消息，latest 最新的消息
# consumer = KafkaConsumer('test', bootstrap_servers=['localhost:9092'], auto_offset_reset='earliest')
# 订阅要消费的主题,消费者-订阅多个主题
# consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'])
# consumer.subscribe(topics=['test', 'test0'])
consumer = KafkaConsumer('test', bootstrap_servers=['localhost:9092'])

# # 获取test主题的分区信息
# print consumer.partitions_for_topic('test')
# # 获取主题列表
# print consumer.topics()
# # 获取当前消费者订阅的主题
# print consumer.subscription()
# # 获取当前消费者topic、分区信息
# print consumer.assignment()
# # 获取当前主题的最新偏移量
# print consumer.position(TopicPartition(topic='test', partition=0))
# # 重置偏移量，从第1个偏移量消费
# consumer.seek(TopicPartition(topic='test', partition=0), 1)

for message in consumer:
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value))

while True:
    msg = consumer.poll(timeout_ms=5)
    print(msg)
    time.sleep(1)
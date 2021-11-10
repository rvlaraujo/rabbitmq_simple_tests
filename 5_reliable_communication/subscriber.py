import pika
import random
import time

subId = random.randint(1, 100)
print('Subscriger ID = ', subId)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs_exchange',
                         exchange_type='direct', durable=True)

queue_name = 'task_queue'
result = channel.queue_declare(queue=queue_name, durable=True)

severity = ['Error', 'Warning', 'Info', 'Other']

for s in severity:
    channel.queue_bind(exchange='logs_exchange',
                       queue=queue_name, routing_key=s)
    
print('[*] Waiting for messages')

def callback(ch, method, properties, body):
  print('[x] Received message:::: %r' %body)
  randomSleep = random.randint(3,6)
  print('Working for ', randomSleep, ' seconds')
  while randomSleep > 0:
    print('.', end='')
    time.sleep(1)
    randomSleep -= 1
  print("!")
  ch.basic_ack(delivery_tag=method.delivery_tag)
  
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=queue_name, on_message_callback=callback)

channel.start_consuming()

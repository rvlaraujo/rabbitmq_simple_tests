import pika

# 1 - Create a connection say CN
connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
# 2 - Create a channel in CH, say CH
channel = connection.channel()
# 3 - Create the exchange (will not affect if exchange is already there)
channel.exchange_declare(exchange = 'br_exchange', exchange_type = 'fanout')

# 4 - Create the temporary queue, if it does not exist already and associate it with the channel CH EXCLUSIVELY
result = channel.queue_declare(queue = '', exclusive = True)
queue_name = result.method.queue
print("Subscriber queue_name =", queue_name)

# 5 - Bind the queue with the exchange
channel.queue_bind(exchange = 'br_exchange', queue = queue_name)

print('[*] waiting for the messages')

# 6 - Associate a call-back function with the message queue
def callback(ch, method, properties, body):
  print('[*] %r' %body)
  
# 7 - Start consuming the messages. 'auto_ack' with True will delete the message from queue after it is consumed
channel.basic_consume(queue = queue_name, on_message_callback = callback, auto_ack = True)
channel.start_consuming()

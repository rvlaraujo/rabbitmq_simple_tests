import pika

# 1 - Create a connection, say CN
coonection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# 2 - Create a channel in CN, say CH
channel = coonection.channel()

# 3 - Create an Exchange and Specify the broadcast
channel.exchange_declare(exchange = 'br_exchange', exchange_type = 'fanout')

# 4 - Publish message
for i in range(4):
  message = f'Hello {i}'
  channel.basic_publish(exchange = 'br_exchange', routing_key = '', body = message)
  print(f'[x] sent {message}')

# 4 - Publish the message
channel.basic_publish(exchange="", routing_key="hello", body="hello, I'm your Seond Message")
print("[x] Sent Hello Message")

# 5 - Delete the Exchange after send messages
channel.exchange_delete(exchange = 'br_exchange', if_unused = False)

# 6 - Close the connection Automatically closes the channel
coonection.close()
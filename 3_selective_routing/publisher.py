import pika
import sys
import random

# 1 - Create a connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# 2 - Create a channel
channel = connection.channel()

# 3 - Create an Exchange
channel.exchange_declare(exchange='logs_exchange', exchange_type='direct')

severity = ['Error', 'Warning', 'Info', 'Other']
messages = ['EMsg', 'WMsg', 'IMsg', 'OMsg']

# 4 - Publish the messages
for i in range(10):
    randomNum = random.randint(0, len(severity)-1)
    print(randomNum)
    message = messages[randomNum]
    severity_routing_key = severity[randomNum]
    # publish the message with specific Routing_Key in the channel
    channel.basic_publish(exchange='logs_exchange',
                          routing_key=severity_routing_key, body=message)
    print("[x] send %r" % message)

# 5 - Close the connection
channel.exchange_delete(exchange='logs_exchante', if_unused=False)
connection.close()

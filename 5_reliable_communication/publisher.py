import pika
import sys
import random

# Creating a Connection and given the channel
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Channel verify if the messages are delivered
channel.confirm_delivery()

# Binding channel to the Exchange and make it 'persistent' after reboot or fails
channel.exchange_declare(exchange='logs_exchange',
                         exchange_type='direct', durable=True)

severity = ['Error', 'Warning', 'Infor', 'Other']
messages = ['EMsg', 'WMsg', 'IMsg', 'OMsg']

# Publishing messages in the channel
for i in range(10):
    randomNum = random.randint(0, len(severity) - 1)
    message = messages[randomNum]
    rk = severity[randomNum]
    try:
        channel.basic_publish(exchange='logs_exchange', routing_key=rk,
                              body=message, properties=pika.BasicProperties(delivery_mode=2))
        print("[x] send %r" %message)
    except pika.exceptions.ChannelClosed:
      print('Channel Closed')
    except pika.exceptions.ConnectionClosed:
      print('Connection Closed')

channel.exchange_delete(exchange='logs_exchange', if_unused=False)
connection.close()

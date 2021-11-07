import pika
import sys
import random

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='system_exchange',
                         exchange_type='topic', durable=False)

severity = ['E', 'W', 'I']
priority = ['H', 'M', 'L']
action = ['A1', 'A2', 'A3']
component = ['C1', 'C2', 'C3']


for i in range(10):
    randomSeverity = severity[random.randint(0, len(severity) - 1)]
    randomPriority = priority[random.randint(0, len(priority) - 1)]
    randomAction = action[random.randint(0, len(action) - 1)]
    randomComponent = component[random.randint(0, len(component) - 1)]

    topic_routing_key = "{s}.{p}.{a}.{c}".format(
        s=randomSeverity, p=randomPriority, a=randomAction, c=randomComponent)
    message = topic_routing_key + " :::: <Message>"

    channel.basic_publish(exchange='system_exchange',
                          routing_key=topic_routing_key, body=message)
    print("[x] sent %r" % message)

# Comment the line below for not destroy the exchange after messages are send to the broker
channel.exchange_delete(exchange='system_exchange', if_unused=False)

connection.close()

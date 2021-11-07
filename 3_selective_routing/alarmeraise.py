import pika

# 1 - create a connection
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

# 2 - Create a channel
channel = connection.channel()

# 3 - Create and configure an Exchange
channel.exchange_declare(exchange='logs_exchange', exchange_type='direct')
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# 4 - Type of routing_keys is wainting for consume
severity = ['Error', 'Warning', 'Info']

# 5 - bind the queue with the exchange for the required Routing Keys
channel.queue_bind(exchange='logs_exchange',
                   queue=queue_name, routing_key='Error')
channel.queue_bind(exchange='logs_exchange',
                   queue=queue_name, routing_key='Warning')

print('[*] waiting for the messages')


def callback(ch, method, properties, body):
    print('[x] Alarm::: %r' %body)


# 6 - Consume the messages
channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
import pika

# 1 -> Creating a Connection and Channel in the Producer/Consumer
# Create a connection, say CN
coonection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# Create a channel in CN, say CH
channel = coonection.channel()

# 2 - Create an Exchange and Specify the bindings
# This step is not required in thes example, as we are working with default exchange

# 3- If the queue does not exist already, create a queue through the channel
channel.queue_declare(queue="hello")

# 4 - Publish the message
channel.basic_publish(exchange="", routing_key="hello", body="hello, I'm your Seond Message")
print("[x] Sent Hello Message")

# 5 - Close the connection Automatically closes the channel
coonection.close()
import pika, sys, os

def main():
  # 1 -> Creating a Connection and Channel in the Producer/Consumer
  # Create a connection, say CN
  coonection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
  # Create a channel in CN, say CH
  channel = coonection.channel()

  # 2 - Create an Exchange and Specify the bindings
  # This step is not required in thes example, as we are working with default exchange

  # 3- If the queue does not exist already, create a queue through the channel
  channel.queue_declare(queue="hello")

  def callback(ch, method, properties, body):
    print("[x] received %r" %body)
    
  # 4 - Associate a call-back funciont with the message queue
  channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack = True)

  # 5 - Start consuming the message
  print(" [*] waiting for the messages. To exist press Ctrl-C")
  channel.start_consuming()


## Start the exexample
if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    print("Interrupted")
    try:
      sys.exit(0)
    except SystemExit:
      os._exit(0)
# RabbitMQ Python

This is a collection of Python scripts to test AMQP Protocol implemented by [RabbitMQ](https://www.rabbitmq.com/) message broker.

## Requirements to run the scprits

To run the scripts you'll need:

- Python 3.9.7+
- RabbitMQ 3.7.9
- Erlang 24.1.2
- [pika 1.2.0](https://pypi.org/project/pika/)

### Run RabbitMQ via Docker

I used the official Docker Image for RabbitMQ for running my examples. You will find it [here](https://hub.docker.com/_/rabbitmq).

Before run the examples, you must start the container with the following command:

```bash
docker run --rm -it -p 15672:15672 -p 5672:5672 rabbitmq:3-management
```

To access the RabbitMQ web interface, go to [http://localhost:15672/](http://localhost:15672/) and fill the username and password with 'guest'.

## The examples Scripts

### 1 - Simple Queue

In the folder 1_simplequeue you can find a basic implementation of a consumer and producer to work with RabbitMQ in Basic approach.
In this approach, the exechange implements a round-robin maner to send message to the consumers by the queue.

First run the consumer.py script and then runs the producer.py script.

### 2 - Fanout (Broadcast)

In the folder 2_fanout you can find a implementation of broadcast approuch, where one publish send messeges to the Message Broker and then
are delivery tho the one (or no one) or more subscribers.

First, run the one or more subscribers and then runs the publisher.py script


### 3 - Selective Routing

In the folder 3_selective_routing, you can find an implementation of a Selective Routing approuch, which is used the Default Exchange to incoming messages to the subscribers, when they create the binding rules in the Exchange.

First you must run the subscribers (screenprinter.py, filewriter.py and alarmeraise.py) and so then runs the publisher. This is important since the messages what are incoming with no has binding rules, all messages are discarded for the Exchange.

### 4 - Topic Exchange

The folder 4_topic_exchange has an implemmentation of a Topic Exchange based on multiple patterns.

First you must execute the subscribers and so then run the publisher. If the exchange is deleted, the binging rules are lost.


import pika

class QueueWrapper:

    def __init__(self, address):
        params = pika.URLParameters(address)
        self.connection = pika.BlockingConnection(params)
        self.channel = self.connection.channel()

    def publish(self, queueName, message):
        self.channel.queue_declare(queue=queueName)
        self.channel.basic_publish(exchange="", routing_key=queueName, body=message)

    def receive(self, queueName, callback_caller, stopAfterReceived):
        self.callback_caller = callback_caller
        self.stopAfterReceived = stopAfterReceived
        self.channel.queue_declare(queue=queueName)
        self.channel.basic_consume(queue=queueName, on_message_callback=self.callback_internal, auto_ack=True)
        try:
            self.channel.start_consuming()
        except KeyboardInterrupt:
            self.channel.stop_consuming()

    def callback_internal(self, channel, method, properties, body):
        self.callback_caller(body)
        if self.stopAfterReceived:
            self.channel.stop_consuming()
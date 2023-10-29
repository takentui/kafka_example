import pika
import json
import time

from app.config import rabbit, RabbitSettings


class PikaPublisher:

    def __init__(self, cfg: RabbitSettings):
        self._cfg = cfg
        self.queue_name = cfg.queue_name

    def initialize(self):
        self.credentials = pika.PlainCredentials('guest', 'guest')
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host=self._cfg.host, port=self._cfg.port,
                                                                             credentials=self.credentials))
        self._channel = self._connection.channel()
        self._channel.exchange_declare(exchange=self._cfg.exchange_name, exchange_type=self._cfg.exchange_type)

    def close(self):
        self._connection.close()

    def send_message(self, message_type, message):
        self.initialize()
        message = json.dumps({'type': message_type, 'message': message})
        self._channel.basic_publish(exchange=self._cfg.exchange_name, routing_key=self._cfg.queue_name, body=message)
        self.close()



rabbit_publisher = PikaPublisher(rabbit)

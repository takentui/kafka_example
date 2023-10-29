import logging

import pika
import json
import time

from app.config import rabbit, RabbitSettings


class PikaConsumer:

    def __init__(self, cfg: RabbitSettings):
        self._cfg = cfg
        self.queue_name = cfg.queue_name

    def initialize(self):
        self.credentials = pika.PlainCredentials('guest', 'guest')
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host=self._cfg.host, port=self._cfg.port,
                                                                             credentials=self.credentials))
        self._channel = self._connection.channel()
        self._channel.exchange_declare(exchange=self._cfg.exchange_name, exchange_type=self._cfg.exchange_type)

        self._result = self._channel.queue_declare(queue='', exclusive=True)
        self._queue_name = self._result.method.queue

        self._channel.queue_bind(exchange=self._cfg.exchange_name, queue=self._queue_name)

    def callback(self, ch, method, properties, body):
        logging.warning("Message was received -  processing it...")
        print(f" [xxx] {body}")

    def close(self):
        self._connection.close()

    def receive_message(self):
        self.initialize()
        self._channel.basic_consume(
            queue=self._queue_name, on_message_callback=self.callback, auto_ack=True)
        self._channel.start_consuming()
        self.close()



rabbit_consumer = PikaConsumer(rabbit)

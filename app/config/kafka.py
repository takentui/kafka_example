from typing import Protocol

from pydantic import BaseSettings

from app.config.types import PostgresDsn


class KafkaSettings(BaseSettings):
    bootstrap_servers: list[str] = ["kafka:9092"]
    topic: str = "test-topic"

    class Config:
        env_prefix = "kafka_"

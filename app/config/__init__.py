__all__ = ["application", "database", "kafka", "rabbit", "LOGGING"]

from .app import AppSettings
from .db import DBSettings
from .kafka import KafkaSettings
from .rabbit import RabbitSettings
import logging.handlers

application: AppSettings = AppSettings()  # type: ignore[call-arg]
database: DBSettings = DBSettings()  # type: ignore[call-arg]
kafka: KafkaSettings = KafkaSettings()  # type: ignore[call-arg]
rabbit: RabbitSettings = RabbitSettings()  # type: ignore[call-arg]


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[%(asctime)s %(levelname)s] %(name)s | %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "level": application.log_level,
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "file_handler": {
            "level": application.log_level,
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "app/logs/fastapi-elk-stack.log",
            "mode": "a",
            "maxBytes": 15000000,
            "backupCount": 5,
            "formatter": "verbose",
        },
    },
    "loggers": {
        "": {
            "handlers": ["console", "file_handler"],
            "level": "INFO",
            "propagate": False,
        },
        "app": {
            "handlers": ["console", "file_handler"],
            "level": application.log_level,
            "propagate": False,
        },
        "gunicorn": {
            "handlers": ["console", "file_handler"],
            "level": application.log_level,
            "propagate": False,
        },
        "uvicorn": {
            "handlers": ["console", "file_handler"],
            "level": application.log_level,
            "propagate": False,
        },
        "root": {
            "handlers": ["console", "file_handler"],
            "level": application.log_level,
            "propagate": False,
        },
    },
}

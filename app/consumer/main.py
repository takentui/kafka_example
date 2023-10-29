from app.consumer.rabbit_consumer import rabbit_consumer


def main() -> None:
    rabbit_consumer.receive_message()


if __name__ == "__main__":
    main()

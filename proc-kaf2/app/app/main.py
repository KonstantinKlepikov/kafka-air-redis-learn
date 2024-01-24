import time
import os
import confluent_kafka


HOST = os.environ['HOST']
TOPIC = os.environ['TOPIC']
GROUP = os.environ['GROUP']


def confluent_kafka_consumer(pause: int = 10) -> None:
    """Listen kafka topic
    """

    consumer = confluent_kafka.Consumer({
        'bootstrap.servers': HOST,
        'group.id': GROUP,
        'auto.offset.reset': 'earliest',
        "api.version.request": True,
        })
    consumer.subscribe([TOPIC, ])

    while True:
        try:
            message = consumer.poll(10.0)

            if not message:
                time.sleep(pause)

            if message:
                print(
                    f"{consumer} received message: " +
                    str(message.value().decode('utf-8'))
                        )

        except Exception as e:
            print(f"{consumer} excepted: {str(e)}")


if __name__ == "__main__":


    confluent_kafka_consumer()

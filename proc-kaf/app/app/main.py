import time
import os
import threading
from kafka import KafkaConsumer


HOST = os.environ['HOST']
TOPIC = os.environ['TOPIC']


def python_kafka_consumer(pause: int = 10) -> None:
    """Listen kafka topic
    """
    consumer1 = KafkaConsumer(
        bootstrap_servers=HOST,
        auto_offset_reset='earliest',
        api_version=(3, 6, 1)
    )
    consumer1.subscribe([TOPIC, ])


    while True:
        try:
            message = consumer1.poll(10.0)

            if not message:
                time.sleep(pause)

            if message:
                for consuming_records in message.values():
                    for consumer_record in consuming_records:
                        print(
                            f"{consumer1} received message: " +
                            str(consumer_record.value.decode('utf-8'))
                                )

        except Exception as e:
            print(f"{consumer1} excepted: {str(e)}")


if __name__ == "__main__":


    threads = [
        threading.Thread(target=python_kafka_consumer)
    ]

    while threads:
        t = threads.pop()
        t.start()
        t.join()

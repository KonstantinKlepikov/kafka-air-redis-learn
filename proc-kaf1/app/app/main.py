import time
import os
import kafka


HOST = os.environ['HOST']
TOPIC = os.environ['TOPIC']
GROUP = os.environ['GROUP']


def python_kafka_consumer(pause: int = 10) -> None:
    """Listen kafka topic
    """
    consumer = kafka.KafkaConsumer(
        bootstrap_servers=HOST,
        group_id=GROUP,
        auto_offset_reset='earliest',
        api_version=(3, 6, 1)
    )
    consumer.subscribe([TOPIC, ])

    while True:
        try:
            message = consumer.poll(10.0)

            if not message:
                time.sleep(pause)

            if message:
                for consuming_records in message.values():
                    for consumer_record in consuming_records:
                        print(
                            f"{consumer} received message: " +
                            str(consumer_record.value.decode('utf-8'))
                                )

        except Exception as e:
            print(f"{consumer} excepted: {str(e)}")


if __name__ == "__main__":


        python_kafka_consumer()
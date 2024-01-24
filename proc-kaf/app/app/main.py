import time
import os
import asyncio
import threading
import kafka
import confluent_kafka
import aiokafka


HOST = os.environ['HOST']
TOPIC = os.environ['TOPIC']


def python_kafka_consumer(pause: int = 10) -> None:
    """Listen kafka topic
    """
    consumer = kafka.KafkaConsumer(
        bootstrap_servers=HOST,
        group_id='kafka_python',
        auto_offset_reset='earliest',
        api_version=(3, 6, 1)
    )
    consumer.assign([kafka.TopicPartition(TOPIC, 0)])

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


def confluent_kafka_consumer(pause: int = 10) -> None:
    """Listen kafka topic
    """

    consumer = confluent_kafka.Consumer({
        'bootstrap.servers': HOST,
        'group.id': 'confluent',
        'auto.offset.reset': 'earliest',
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


async def aiokafka_consumer(pause: int = 10, part: int = 0) -> None:
    """Listen kafka topic
    """

    consumer = aiokafka.AIOKafkaConsumer(
        group_id='aiokafka',
        bootstrap_servers=[HOST, ],
            )
    await consumer.start()

    tp = aiokafka.TopicPartition(TOPIC, part)
    consumer.assign([tp, ])

    while True:
        try:
            message = await consumer.getone()

            if not message:
                time.sleep(pause)

            if message:
                print(
                    f"{consumer} received message: " +
                    str(message.value)
                        )

        except Exception as e:
            print(f"{consumer} excepted: {str(e)}")


async def callback(part: int = 0):
    await aiokafka_consumer(part)


def aiokafka_processing():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(callback())
    loop.close()


if __name__ == "__main__":


    threads = [
        threading.Thread(target=python_kafka_consumer),
        threading.Thread(target=confluent_kafka_consumer),
        threading.Thread(target=aiokafka_processing),
    ]

    while threads:
        t = threads.pop()
        t.start()
        t.join()

import time
import os
import asyncio
import aiokafka


HOST = os.environ['HOST']
TOPIC = os.environ['TOPIC']
GROUP = os.environ['GROUP']


async def aiokafka_consumer(pause: int = 10) -> None:
    """Listen kafka topic
    """

    consumer = aiokafka.AIOKafkaConsumer(
        TOPIC,
        group_id=GROUP,
        bootstrap_servers=[HOST, ],
            )
    await consumer.start()

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


if __name__ == "__main__":


    asyncio.run(aiokafka_consumer())

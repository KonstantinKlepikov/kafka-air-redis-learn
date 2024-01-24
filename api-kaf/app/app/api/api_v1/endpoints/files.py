import json
import confluent_kafka
import kafka
from fastapi import APIRouter, status
from app.config import settings


router = APIRouter()
producer1 = kafka.KafkaProducer(
    bootstrap_servers=settings.HOST,
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    api_version=(3, 6, 1),
        )
producer2 = confluent_kafka.Producer({'bootstrap.servers': settings.HOST})


def delivery_report(err, msg):
    """
    Called once for each message produced to indicate delivery result.
    Triggered by poll() or flush().
    """
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')


def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)


def on_send_error(excp):
    print('I am an errback', exc_info=excp)


@router.post(
    "/kafka_python",
    status_code=status.HTTP_200_OK,
    summary='Send to kafka data. Here we use kafka-python package',
    response_description="Sent to kafka.",
    responses=settings.ERRORS
        )
def send_kafka_python(user_id: int, user_name: str) -> None:
    """Send data to kafka data
    """
    producer1.send(
        settings.TOPIC,
        {user_id: user_name},
            ).add_callback(on_send_success).add_errback(on_send_error)


@router.post(
    "/confluent_kafka",
    status_code=status.HTTP_200_OK,
    summary='Send to kafka data. Here we use confluent-kafka package',
    response_description="Sent to kafka.",
    responses=settings.ERRORS
        )
def send_confluent_kafka(user_id: int, user_name: str) -> None:
    """Send data to kafka
    """
    producer2.poll(0)
    producer2.produce(
        settings.TOPIC,
        json.dumps({user_id: user_name}).encode('utf-8'),
        callback=delivery_report,
            )


@router.post(
    "/aiokafka",
    status_code=status.HTTP_200_OK,
    summary='Send to kafka data. Here we use aiokafka package',
    response_description="Sent to kafka.",
    responses=settings.ERRORS
        )
def send_aiokafka(user_id: int, user_name: str) -> None:
    """Send data to kafka
    """

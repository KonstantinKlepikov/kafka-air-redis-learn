import json
from fastapi import APIRouter, status
from kafka import KafkaProducer
from app.config import settings


router = APIRouter()


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
def send(user_id: int, user_name: str) -> None:
    """Send to kafka data
    """
    producer = KafkaProducer(
        bootstrap_servers=settings.HOST,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )
    producer.send(
        settings.TOPIC,
        {user_id: user_name},
        ).add_callback(on_send_success).add_errback(on_send_error)

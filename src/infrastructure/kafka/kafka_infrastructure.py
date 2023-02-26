from kafka import KafkaProducer

from decouple import config

class KafkaInfrastructure:
    __producer = None

    @classmethod
    async def get_producer(cls) -> KafkaProducer:
        if cls.__producer is None:
            producer_config = {
                "bootstrap_servers": config("KAFKA_URL"),
                "client_id": config("CLIENT_ID")
            }

            cls.__producer = KafkaProducer(**producer_config)

        return cls.__producer


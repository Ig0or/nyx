from decouple import config

from src.domain.validators.stock_market.stock_market_validators import StockOrderValidator
from src.infrastructure.kafka.kafka_infrastructure import KafkaInfrastructure


class StockMarketService:
    __kafka_infrastructure = KafkaInfrastructure

    @classmethod
    async def __send_oder_to_topic(cls, order_input: dict):
        kafka_producer = await cls.__kafka_infrastructure.get_producer()

        topic_name = config("TOPIC_NAME")

        kafka_producer.send(topic=topic_name, key=order_input.get("symbol"), value=order_input)




    @classmethod
    async def send_order(cls, order_input: StockOrderValidator):
        order_input_dict = order_input.dict()








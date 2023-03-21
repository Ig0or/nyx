# Standard
from typing import NoReturn

# Third Party
from decouple import config

# Local
from src.domain.models.stock_market.order_model import OrderModel
from src.infrastructure.kafka.kafka_infrastructure import KafkaInfrastructure
from src.infrastructure.mongodb.mongodb_infrastructure import MongoDBInfrastructure


class StockMarketRepository:
    @staticmethod
    async def create_order_on_database(order_model: OrderModel) -> NoReturn:
        connection = MongoDBInfrastructure.get_connection()
        connection.insert_one(order_model.copy())

        return

    @classmethod
    async def send_order_to_kafka_topic(cls, order_model: OrderModel) -> NoReturn:
        topic_name = config("KAFKA_TOPIC_NAME")

        producer = KafkaInfrastructure.get_producer()
        producer.send(topic=topic_name, key=order_model["symbol"], value=order_model)
        producer.flush()

        return

    @staticmethod
    async def get_all_orders() -> list[dict]:
        connection = MongoDBInfrastructure.get_connection()

        orders = connection.find({}, {"_id": 0})
        orders_list = list(orders)

        return orders_list

    @staticmethod
    async def get_order_by_id(order_id: str) -> dict:
        connection = MongoDBInfrastructure.get_connection()

        order = connection.find_one({"order_id": order_id}, {"_id": 0})

        return order

# Third Party
from uuid import uuid4

# Local
from src.domain.enums.stock_market.stock_market_enums import OrderStatusEnum
from src.domain.models.stock_market.order_model import OrderModel
from src.domain.validators.stock_market.stock_market_validators import (
    StockOrderValidator,
)
from src.repositories.stock_market.stock_market_repository import StockMarketRepository


class StockMarketService:
    @staticmethod
    def __create_order_model(order_input: StockOrderValidator) -> OrderModel:
        order_model: OrderModel = {
            "symbol": order_input.symbol,
            "quantity": order_input.quantity,
            "price": order_input.price,
            "order_type": order_input.order_type,
            "order_status": OrderStatusEnum.PENDING,
            "order_id": str(uuid4()),
        }

        return order_model

    @classmethod
    async def send_order(cls, order_input: StockOrderValidator) -> OrderModel:
        order_model = cls.__create_order_model(order_input=order_input)

        await StockMarketRepository.create_order_on_database(order_model=order_model)
        await StockMarketRepository.send_order_to_kafka_topic(order_model=order_model)

        return order_model

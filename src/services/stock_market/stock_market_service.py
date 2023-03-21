# Local
from src.domain.dtos.stock_market.resumed_order_dto import ResumedOrderDto
from src.domain.extensions.stock_market.order_extension import OrderExtension
from src.domain.validators.stock_market.order_validator import (
    OrderValidator,
)
from src.repositories.stock_market.stock_market_repository import StockMarketRepository


class StockMarketService:
    @staticmethod
    async def send_order(order_input: OrderValidator) -> ResumedOrderDto:
        order_model = OrderExtension.create_new_order_model(order_input=order_input)

        await StockMarketRepository.create_order_on_database(order_model=order_model)
        await StockMarketRepository.send_order_to_kafka_topic(order_model=order_model)

        resumed_order_dto = OrderExtension.to_resumed_order_dto(order_model=order_model)

        return resumed_order_dto

    @classmethod
    async def list_orders(cls):
        orders = await StockMarketRepository.get_all_orders()
        simplified_orders_model = OrderExtension.to_array_simplified_order_model(
            orders=orders
        )

        return simplified_orders_model

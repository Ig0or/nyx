# Local
from src.domain.extensions.stock_market.order_extension import OrderExtension
from src.domain.models.stock_market.order_model import OrderModel
from src.domain.models.stock_market.simplified_order_model import SimplifiedOrderModel
from src.domain.validators.stock_market.stock_market_validators import (
    StockOrderValidator,
)
from src.repositories.stock_market.stock_market_repository import StockMarketRepository


class StockMarketService:
    @staticmethod
    async def send_order(order_input: StockOrderValidator) -> OrderModel:
        order_model = OrderExtension.create_new_order_model(order_input=order_input)

        await StockMarketRepository.create_order_on_database(order_model=order_model)
        await StockMarketRepository.send_order_to_kafka_topic(order_model=order_model)

        return order_model

    @classmethod
    async def list_orders(cls) -> list[SimplifiedOrderModel]:
        orders = await StockMarketRepository.get_all_orders()
        simplified_orders_model = OrderExtension.to_array_simplified_order_model(
            orders=orders
        )

        return simplified_orders_model

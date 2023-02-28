# Local
from src.domain.models.stock_market.order_model import OrderModel
from src.domain.models.stock_market.simplified_order_model import SimplifiedOrderModel
from src.domain.validators.stock_market.stock_market_validators import (
    StockOrderValidator,
)
from src.services.stock_market.stock_market_service import StockMarketService


class StockMarketController:
    @staticmethod
    async def send_order(order_input: StockOrderValidator) -> OrderModel:
        response = await StockMarketService.send_order(order_input=order_input)

        return response

    @staticmethod
    async def list_orders() -> list[SimplifiedOrderModel]:
        response = await StockMarketService.list_orders()

        return response

# Local
from http import HTTPStatus

from src.domain.dtos.stock_market.resumed_order_dto import ResumedOrderResponseDto
from src.domain.models.stock_market.order_model import OrderModel
from src.domain.models.stock_market.simplified_order_model import SimplifiedOrderModel
from src.domain.validators.stock_market.order_validator import (
    OrderValidator,
)
from src.services.stock_market.stock_market_service import StockMarketService


class StockMarketController:
    @staticmethod
    async def send_order(order_input: OrderValidator) -> ResumedOrderResponseDto:
        response = await StockMarketService.send_order(order_input=order_input)

        response: ResumedOrderResponseDto = {
            "result": response,
            "message": "The order was created",
            "success": True,
            "status_code": HTTPStatus.CREATED
        }

        return response

    @staticmethod
    async def list_orders() -> list[SimplifiedOrderModel]:
        response = await StockMarketService.list_orders()

        return response

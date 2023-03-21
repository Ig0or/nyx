# Local
from http import HTTPStatus

from src.domain.dtos.stock_market.resumed_order_dto import (
    ResumedOrderResponseDto,
)
from src.domain.validators.stock_market.order_validator import (
    OrderValidator,
)
from src.services.stock_market.stock_market_service import StockMarketService


class StockMarketController:
    @staticmethod
    async def send_order(order_input: OrderValidator) -> ResumedOrderResponseDto:
        result = await StockMarketService.send_order(order_input=order_input)

        response: ResumedOrderResponseDto = {
            "result": result,
            "message": "The order was created",
            "success": True,
            "status_code": HTTPStatus.CREATED,
        }

        return response

    @staticmethod
    async def list_orders():
        response = await StockMarketService.list_orders()

        return response

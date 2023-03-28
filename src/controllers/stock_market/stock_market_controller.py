# Standard
from http import HTTPStatus

# Local
from src.domain.dtos.stock_market.detailed_order_dto import DetailedOrderResponseDto
from src.domain.dtos.stock_market.resumed_order_dto import (
    ListResumedOrderResponseDto,
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
    async def list_orders() -> ListResumedOrderResponseDto:
        result = await StockMarketService.list_orders()

        response: ListResumedOrderResponseDto = {
            "result": result,
            "success": True,
            "status_code": HTTPStatus.OK,
        }

        return response

    @staticmethod
    async def detail_order(order_id: str) -> DetailedOrderResponseDto:
        result = await StockMarketService.detail_order(order_id=order_id)

        response: DetailedOrderResponseDto = {
            "result": result,
            "success": True,
            "status_code": HTTPStatus.OK,
        }

        return response

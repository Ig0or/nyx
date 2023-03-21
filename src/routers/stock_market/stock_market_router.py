# Third Party
from fastapi import APIRouter, Response

# Local
from src.controllers.stock_market.stock_market_controller import StockMarketController
from src.domain.dtos.stock_market.resumed_order_dto import (
    ResumedOrderResponseDto,
    ListResumedOrderResponseDto,
)
from src.domain.validators.stock_market.order_validator import (
    OrderValidator,
)
from src.entry_points.stock_market.stock_market_entry_point import StockMarketEntryPoint


class StockMarketRouter:
    __stock_market_router = APIRouter(prefix="/stock_market", tags=["StockMarket"])

    @classmethod
    def get_routers(cls) -> APIRouter:
        return cls.__stock_market_router

    @staticmethod
    @__stock_market_router.post("/send_order", response_model=ResumedOrderResponseDto)
    async def send_order(order_input: OrderValidator) -> Response:
        response = await StockMarketEntryPoint.process_request(
            callback=StockMarketController.send_order, order_input=order_input
        )

        return response

    @staticmethod
    @__stock_market_router.get(
        "/list_orders", response_model=ListResumedOrderResponseDto
    )
    async def list_orders() -> Response:
        response = await StockMarketEntryPoint.process_request(
            callback=StockMarketController.list_orders
        )

        return response

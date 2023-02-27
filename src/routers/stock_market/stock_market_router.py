# Third Party
from fastapi import APIRouter

# Local
from src.controllers.stock_market.stock_market_controller import StockMarketController
from src.domain.models.stock_market.order_model import OrderModel
from src.domain.validators.stock_market.stock_market_validators import (
    StockOrderValidator,
)


class StockMarketRouter:
    __stock_market_router = APIRouter()

    @classmethod
    def get_routers(cls) -> APIRouter:
        return cls.__stock_market_router

    @staticmethod
    @__stock_market_router.post("/stock_market/send_order")
    async def send_order(order_input: StockOrderValidator) -> OrderModel:
        response = await StockMarketController.send_order(order_input=order_input)

        return response

# Third Party
from fastapi import APIRouter

# Local
from src.controllers.stock_market.stock_market_controller import StockMarketController
from src.domain.models.stock_market.order_model import OrderModel
from src.domain.models.stock_market.simplified_order_model import SimplifiedOrderModel
from src.domain.validators.stock_market.order_validator import (
    OrderValidator,
)


class StockMarketRouter:
    __stock_market_router = APIRouter()

    @classmethod
    def get_routers(cls) -> APIRouter:
        return cls.__stock_market_router

    @staticmethod
    @__stock_market_router.post("/stock_market/send_order")
    async def send_order(order_input: OrderValidator) -> OrderModel:
        response = await StockMarketController.send_order(order_input=order_input)

        return response

    @staticmethod
    @__stock_market_router.get("/stock_market/list_orders")
    async def list_orders() -> list[SimplifiedOrderModel]:
        response = await StockMarketController.list_orders()

        return response

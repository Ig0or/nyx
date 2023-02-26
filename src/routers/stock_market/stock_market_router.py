from fastapi import APIRouter

from src.domain.validators.stock_market.stock_market_validators import StockOrderValidator


class StockMarketRouter:
    __stock_market_router = APIRouter()

    @staticmethod
    def get_routers() -> APIRouter:
        return StockMarketRouter.__stock_market_router

    @staticmethod
    @__stock_market_router.post('/stock_market/send_order')
    async def send_order(order_input: StockOrderValidator):

        return "Ok"


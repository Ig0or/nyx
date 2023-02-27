# Third Party
from fastapi import FastAPI

# Standard
from typing_extensions import NoReturn

# Local
from src.routers.stock_market.stock_market_router import StockMarketRouter


class BaseRouter:
    __app = FastAPI()

    @classmethod
    def __register_stock_market_routers(cls) -> NoReturn:
        stock_market_routers = StockMarketRouter.get_routers()

        cls.__app.include_router(router=stock_market_routers)

    @classmethod
    def register_routers(cls):
        cls.__register_stock_market_routers()

        return cls.__app

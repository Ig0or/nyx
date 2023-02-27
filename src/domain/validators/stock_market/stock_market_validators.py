# Third Party
from pydantic import BaseModel

# Local
from src.domain.enums.stock_market.stock_market_enums import OrdersTypeEnum


class StockOrderValidator(BaseModel):
    symbol: str
    quantity: int
    price: float
    order_type: OrdersTypeEnum

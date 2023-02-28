# Standard
from typing import TypedDict

# Local
from src.domain.enums.stock_market.stock_market_enums import (
    OrderStatusEnum,
)


class SimplifiedOrderModel(TypedDict):
    symbol: str
    order_status: OrderStatusEnum
    order_id: str

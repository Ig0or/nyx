# Standard
from typing_extensions import NotRequired, TypedDict

# Local
from src.domain.enums.stock_market.stock_market_enum import OrderStatusEnum


class DetailedOrderDto(TypedDict):
    symbol: str
    quantity: int
    unit_price: NotRequired[float]
    total_price: NotRequired[float]
    order_status: OrderStatusEnum
    order_message: NotRequired[str]
    order_id: str


class DetailedOrderResponseDto(TypedDict):
    result: DetailedOrderDto
    message: NotRequired[str]
    success: bool
    status_code: int

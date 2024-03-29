# Standard
from typing_extensions import NotRequired, TypedDict

# Local
from src.domain.enums.stock_market.stock_market_enum import OrderStatusEnum


class ResumedOrderDto(TypedDict):
    symbol: str
    quantity: int
    order_status: OrderStatusEnum
    order_id: str


class ResumedOrderResponseDto(TypedDict):
    result: ResumedOrderDto
    message: NotRequired[str]
    success: bool
    status_code: int


class ListResumedOrderResponseDto(TypedDict):
    result: list[ResumedOrderDto]
    message: NotRequired[str]
    success: bool
    status_code: int

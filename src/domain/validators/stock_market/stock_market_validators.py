# Third Party
from pydantic import BaseModel, validator

# Local
from src.domain.enums.stock_market.stock_market_enums import OrdersTypeEnum


class StockOrderValidator(BaseModel):
    symbol: str
    quantity: int
    price: float
    order_type: OrdersTypeEnum

    @validator("quantity")
    def quantity_check(cls, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")

        return quantity

    @validator("price")
    def price_check(cls, price: int):
        if price <= 0:
            raise ValueError("Price must be greater than 0.")

        return price

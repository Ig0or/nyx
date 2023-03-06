# Third Party
from pydantic import BaseModel, validator


class OrderValidator(BaseModel):
    symbol: str
    quantity: int

    @validator("quantity")
    def quantity_check(cls, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")

        return quantity

# Third Party
from uuid import uuid4

from src.domain.dtos.stock_market.resumed_order_dto import ResumedOrderDto

# Local
from src.domain.enums.stock_market.stock_market_enums import (
    OrderStatusEnum,
)
from src.domain.models.stock_market.order_model import OrderModel
from src.domain.validators.stock_market.order_validator import (
    OrderValidator,
)


class OrderExtension:
    @staticmethod
    def create_new_order_model(order_input: OrderValidator) -> OrderModel:
        order_model: OrderModel = {
            "symbol": order_input.symbol,
            "quantity": order_input.quantity,
            "order_status": OrderStatusEnum.PENDING,
            "order_id": str(uuid4()),
        }

        return order_model

    @staticmethod
    def to_resumed_order_dto(order_model: OrderModel) -> ResumedOrderDto:
        resumed_order_dto: ResumedOrderDto = {
            "symbol": order_model["symbol"],
            "quantity": order_model["quantity"],
            "order_status": order_model["order_status"],
            "order_id": order_model["order_id"],
        }

        return resumed_order_dto

    @staticmethod
    def to_array_simplified_order_model(
        orders: list[dict],
    ):
        simplified_orders_model = list()

        for order in orders:
            simplified_order_model = OrderExtension.to_simplified_order_model(
                order=order
            )
            simplified_orders_model.append(simplified_order_model)

        return simplified_orders_model

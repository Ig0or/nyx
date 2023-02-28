# Third Party
from uuid import uuid4

# Local
from src.domain.enums.stock_market.stock_market_enums import (
    OrderStatusEnum,
)
from src.domain.models.stock_market.order_model import OrderModel
from src.domain.models.stock_market.simplified_order_model import SimplifiedOrderModel
from src.domain.validators.stock_market.stock_market_validators import (
    StockOrderValidator,
)


class OrderExtension:
    @staticmethod
    def create_new_order_model(order_input: StockOrderValidator) -> OrderModel:
        order_model: OrderModel = {
            "symbol": order_input.symbol,
            "quantity": order_input.quantity,
            "price": order_input.price,
            "order_type": order_input.order_type,
            "order_status": OrderStatusEnum.PENDING,
            "order_id": str(uuid4()),
        }

        return order_model

    @staticmethod
    def __to_simplified_order_model(order: dict) -> SimplifiedOrderModel:
        simplified_order_model: SimplifiedOrderModel = {
            "symbol": order.get("symbol", ""),
            "order_status": order.get("order_status", OrderStatusEnum.CANCELLED),
            "order_id": order.get("order_id", ""),
        }

        return simplified_order_model

    @staticmethod
    def to_array_simplified_order_model(
        orders: list[dict],
    ) -> list[SimplifiedOrderModel]:
        simplified_orders_model = list()

        for order in orders:
            simplified_order_model = OrderExtension.__to_simplified_order_model(
                order=order
            )
            simplified_orders_model.append(simplified_order_model)

        return simplified_orders_model

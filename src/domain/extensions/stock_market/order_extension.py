# Third Party
from uuid import uuid4

# Local
from src.domain.dtos.stock_market.detailed_order_dto import DetailedOrderDto
from src.domain.dtos.stock_market.resumed_order_dto import ResumedOrderDto
from src.domain.enums.stock_market.dto_type_enum import DtoTypeEnum
from src.domain.enums.stock_market.stock_market_enum import (
    OrderStatusEnum,
)
from src.domain.models.stock_market.order_model import OrderModel
from src.domain.validators.stock_market.order_validator import (
    OrderValidator,
)


class OrderExtension:
    @staticmethod
    def __to_resumed_order_dto(order_model: OrderModel) -> ResumedOrderDto:
        resumed_order_dto: ResumedOrderDto = {
            "symbol": order_model["symbol"],
            "quantity": order_model["quantity"],
            "order_status": order_model["order_status"],
            "order_id": order_model["order_id"],
        }

        return resumed_order_dto

    @staticmethod
    def __to_detailed_order_dto(order_model: OrderModel) -> DetailedOrderDto:
        order_dto: DetailedOrderDto = {
            "symbol": order_model["symbol"],
            "quantity": order_model["quantity"],
            "unit_price": order_model["unit_price"],
            "total_price": order_model["total_price"],
            "order_status": order_model["order_status"],
            "order_message": order_model["order_message"],
            "order_id": order_model["order_id"],
        }

        return order_dto

    @staticmethod
    def to_order_dto(
        dto_type: DtoTypeEnum, order_model: OrderModel
    ) -> DetailedOrderDto | ResumedOrderDto:
        dto_types = {
            DtoTypeEnum.RESUMED: OrderExtension.__to_resumed_order_dto,
            DtoTypeEnum.DETAILED: OrderExtension.__to_detailed_order_dto,
        }

        dto_type_function = dto_types.get(dto_type)

        order_dto = dto_type_function(order_model=order_model)

        return order_dto

    @staticmethod
    def to_resumed_array_order_dto(orders_model: list[OrderModel]):
        resumed_orders_dto = list()

        for order in orders_model:
            order_dto = OrderExtension.to_order_dto(
                dto_type=DtoTypeEnum.RESUMED, order_model=order
            )

            resumed_orders_dto.append(order_dto)

        return resumed_orders_dto

    @staticmethod
    def to_order_model(order: dict) -> OrderModel:
        order_model: OrderModel = {
            "symbol": order.get("symbol", ""),
            "quantity": order.get("quantity", 0),
            "unit_price": order.get("unit_price", 0),
            "total_price": order.get("total_price", 0),
            "order_status": order.get("order_status", OrderStatusEnum.PENDING),
            "order_message": order.get("order_message", ""),
            "order_id": order.get("order_id", ""),
        }

        return order_model

    @staticmethod
    def to_array_order_model(
        orders: list[dict],
    ) -> list[OrderModel]:
        resumed_orders_model = list()

        for order in orders:
            resumed_order_model = OrderExtension.to_order_model(order=order)
            resumed_orders_model.append(resumed_order_model)

        return resumed_orders_model

    @staticmethod
    def create_new_order_model(order_input: OrderValidator) -> OrderModel:
        order_model: OrderModel = {
            "symbol": order_input.symbol,
            "quantity": order_input.quantity,
            "order_status": OrderStatusEnum.PENDING,
            "order_id": str(uuid4()),
        }

        return order_model

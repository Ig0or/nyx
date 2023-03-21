# Local
from src.domain.dtos.stock_market.detailed_order_dto import DetailedOrderDto
from src.domain.dtos.stock_market.resumed_order_dto import ResumedOrderDto
from src.domain.enums.stock_market.dto_type_enum import DtoTypeEnum
from src.domain.exceptions.stock_market.stock_market_exceptions import OrderNotExists
from src.domain.extensions.stock_market.order_extension import OrderExtension
from src.domain.validators.stock_market.order_validator import (
    OrderValidator,
)
from src.repositories.stock_market.stock_market_repository import StockMarketRepository


class StockMarketService:
    @staticmethod
    async def send_order(order_input: OrderValidator) -> ResumedOrderDto:
        order_model = OrderExtension.create_new_order_model(order_input=order_input)

        await StockMarketRepository.create_order_on_database(order_model=order_model)
        await StockMarketRepository.send_order_to_kafka_topic(order_model=order_model)

        resumed_order_dto = OrderExtension.to_order_dto(
            dto_type=DtoTypeEnum.RESUMED, order_model=order_model
        )

        return resumed_order_dto

    @staticmethod
    async def list_orders() -> list[ResumedOrderDto]:
        orders = await StockMarketRepository.get_all_orders()
        orders_model = OrderExtension.to_array_order_model(orders=orders)

        resumed_orders_dto = OrderExtension.to_resumed_array_order_dto(
            orders_model=orders_model
        )

        return resumed_orders_dto

    @staticmethod
    async def detail_order(order_id: str) -> DetailedOrderDto:
        order = await StockMarketRepository.get_order_by_id(order_id=order_id)

        if not order:
            raise OrderNotExists()

        order_model = OrderExtension.to_order_model(order=order)
        detailed_order_dto = OrderExtension.to_order_dto(dto_type=DtoTypeEnum.DETAILED, order_model=order_model )

        return detailed_order_dto






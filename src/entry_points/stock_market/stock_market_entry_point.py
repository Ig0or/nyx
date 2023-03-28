# Standard
from http import HTTPStatus
from typing import Callable

# Third Party
from fastapi import Response
import loglifos

# Local
from src.domain.dtos.abstract_response.abstract_response_dto import AbstractResponseDto
from src.domain.dtos.response.response_dto import ResponseDto
from src.domain.exceptions.stock_market.stock_market_exceptions import OrderNotExists


class StockMarketEntryPoint:
    @staticmethod
    async def __execute_callback(callback: Callable, **kwargs) -> AbstractResponseDto:
        response = await callback(**kwargs)

        return response

    @staticmethod
    async def process_request(callback: Callable, **kwargs) -> Response:
        response_dto = None

        try:
            response = await StockMarketEntryPoint.__execute_callback(
                callback=callback, **kwargs
            )

            response_dto = ResponseDto(
                success=response.get("success"),
                status_code=response.get("status_code"),
                message=response.get("message"),
                result=response.get("result"),
            )

        except OrderNotExists:
            response_dto = ResponseDto(
                success=False,
                status_code=HTTPStatus.OK,
                message="This order id doesn't exist.",
            )

        except Exception as exception:
            response_dto = ResponseDto(
                success=False,
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                message="An unexpected error occurred.",
            )

            loglifos.error(
                msg="An unexpected exception was raised", exception=exception
            )

        finally:
            http_response = response_dto.build_http_response()

            return http_response

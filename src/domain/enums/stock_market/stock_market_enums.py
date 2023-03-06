# Local
from enum import Enum


class OrderStatusEnum(str, Enum):
    PENDING = "PENDING"
    FINISHED = "FINISHED"
    CANCELLED = "CANCELLED"

from enum import Enum


class OrderStatusEnum(Enum):
    CREATED = 0  # 已创建
    PAID = 1  # 已支付
    DELIVERED = 2  # 已发货
    FINISHED = 3  # 已完成


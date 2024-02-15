from model.UserAddress import UserAddress
from model.GoodsItem import GoodsItem
from model.OrderInfo import OrderInfo
from exception.CommonException import ADDRESS_NOT_EXIST, GOODS_NOT_EXIST, GOODS_STOCK_NOT_ENOUGH, ORDER_NOT_EXIST
from application import db
from service.UserService import UserService
from flask import g
from enums.OrderEnum import OrderStatusEnum
from vo.web.response.PageResponse import build_page_response


def create_order(request):
    openid = g.current_openid
    user = UserService.query_by_openid(openid)

    # 1. 校验地址
    address_id = request.address_id.data
    address = UserAddress.query.get(address_id)
    if not address:
        raise ADDRESS_NOT_EXIST

    # 2. 校验商品
    item_id = request.item_id.data
    item_count = request.item_count.data
    item = GoodsItem.query.with_for_update().filter(GoodsItem.id == item_id).first()
    if not item:
        raise GOODS_NOT_EXIST
    if item.item_stock < item_count:
        raise GOODS_STOCK_NOT_ENOUGH

    # 3. 扣库存
    item.item_stock = item.item_stock - item_count
    db.session.add(item)
    db.session.flush()

    # 4. 创建订单
    order_info = OrderInfo()
    order_info.user_id = user.id
    order_info.item_name = item.item_name
    order_info.item_price = item.item_price
    order_info.item_image = item.main_image
    order_info.item_count = item_count
    order_info.remark = request.remark.data
    order_info.address_name = address.nickname
    order_info.address_mobile = address.mobile
    order_info.address_detail = address.detail
    order_info.status = OrderStatusEnum.CREATED.value

    db.session.add(order_info)
    db.session.commit()

    return order_info.id


def operate_user_order(request):
    """
    c端操作订单
    :param request:
    :return:
    """
    openid = g.current_openid
    user = UserService.query_by_openid(openid)
    order_info = OrderInfo.query.filter_by(id=request.id.data, user_id=user.id).first()
    if not order_info:
        raise ORDER_NOT_EXIST

    return operate_order(request.id.data, request.operate.data)


def operate_order(order_id, operation):
    """
    b端操作订单
    :param order_id:
    :param operation:
    :return:
    """
    order_info = OrderInfo.query.filter_by(id=order_id).first()
    if not order_info:
        raise ORDER_NOT_EXIST
    order_info.status = operation
    db.session.add(order_info)
    db.session.commit()
    return order_info.id


def query_user_order(request):
    openid = g.current_openid
    user = UserService.query_by_openid(openid)

    start_id = request.start_id.data
    page_size = request.page_size.data

    next_id = None

    query = OrderInfo.query.filter(OrderInfo.user_id == user.id, 0 == OrderInfo.is_deleted)
    if request.status.data is not None:
        query = query.filter(OrderInfo.status == request.status.data)
    if start_id > -1:
        query = query.filter(OrderInfo.id < start_id)

    orders = query.order_by(OrderInfo.id.desc()).limit(page_size).all()

    if len(orders) < page_size:
        has_more = False
    else:
        has_more = True
        next_id = orders[-1].id

    return {
        "has_more": str(has_more),
        "next_id": str(next_id),
        "orders": [order.build_info() for order in orders]
    }


def query_order_page(request):
    status = request.status.data
    page_number = request.page_number.data
    page_size = request.page_size.data

    query = OrderInfo.query.filter(0 == OrderInfo.is_deleted)
    if status is not None:
        query = query.filter(OrderInfo.status == status)

    order_count = query.count()
    if order_count == 0:
        return build_page_response([], page_number, page_size, order_count)

    orders = query.order_by(OrderInfo.id.desc()).limit(page_size).offset((page_number - 1) * page_size).all()
    return build_page_response([order.build_info() for order in orders], page_number, page_size, order_count)

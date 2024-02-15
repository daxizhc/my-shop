from flask import request
from service.OrderService import create_order, operate_user_order, query_user_order
from werkzeug.datastructures import ImmutableMultiDict

from utils.HttpResponseUtil import HttpResponseUtil
from www import route_index
from vo.api.request.OrderRequest import CreateOrderRequest, OperateOrderRequest, QueryOrderRequest


@route_index.route("/order/create", methods=["POST"])
def create_goods_order():
    """
    创建订单
    :return: 订单id
    """
    req = CreateOrderRequest(ImmutableMultiDict(request.json))
    if req.validate():
        return HttpResponseUtil.success(create_order(req))
    else:
        return HttpResponseUtil.fail(400, req.errors)


@route_index.route("/order/operate", methods=["POST"])
def operate_goods_order():
    req = OperateOrderRequest(ImmutableMultiDict(request.json))
    if req.validate():
        operate_user_order(req)
        return HttpResponseUtil.success()
    else:
        return HttpResponseUtil.fail(400, req.errors)


@route_index.route("/order/query", methods=["POST"])
def query_goods_order():
    req = QueryOrderRequest(ImmutableMultiDict(request.json))
    if req.validate():
        return HttpResponseUtil.success(query_user_order(req))
    else:
        return HttpResponseUtil.fail(400, req.errors)



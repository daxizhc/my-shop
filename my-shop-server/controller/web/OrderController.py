from flask_login import login_required

from vo.web.request.OrderRequest import OrderPageQueryRequest, OperateOrderRequest
from www import route_admin
from utils.HttpResponseUtil import HttpResponseUtil
from flask import request

from werkzeug.datastructures import ImmutableMultiDict
from service.OrderService import query_order_page, operate_order


@route_admin.route("/order/list", methods=["POST"])
@login_required
def query_order_list():
    """
    获取订单列表
    """
    req = OrderPageQueryRequest(ImmutableMultiDict(request.json))
    if req.validate():
        return HttpResponseUtil.success(query_order_page(req))
    else:
        return HttpResponseUtil.param_error(req.errors)


@route_admin.route("/order/operate", methods=["POST"])
@login_required
def operate_merchant_order():
    """
    操作订单
    """
    req = OperateOrderRequest(ImmutableMultiDict(request.json))
    if req.validate():
        operate_order(req.id.data, req.operate.data)
        return HttpResponseUtil.success()
    else:
        return HttpResponseUtil.param_error(req.errors)


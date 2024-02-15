from flask_login import login_required

from www import route_admin
from vo.web.request.GoodsRequest import GoodsPageQueryRequest, GoodsSaveOrUpdateRequest, GoodsOperateRequest, \
    GoodsStockModifyRequest
from utils.HttpResponseUtil import HttpResponseUtil
from flask import request
from service.GoodsService import GoodsService
from werkzeug.datastructures import ImmutableMultiDict


@route_admin.route("/goods/page", methods=["POST"])
@login_required
def query_goods_list():
    """
    获取商品列表
    :arg: 状态、分类、关键字、页码、每页数量
    :return: 商品图片、商品名称、商品分类、商品价格、商品库存、商品状态
    """
    req = GoodsPageQueryRequest(ImmutableMultiDict(request.json))
    req.category_ids = request.json['category_ids'] if 'category_ids' in request.json else []
    req.status = request.json['status'] if 'status' in request.json else None
    if req.validate():
        return HttpResponseUtil.success(GoodsService.get_goods_page(req))
    else:
        return HttpResponseUtil.param_error(req.errors)


@route_admin.route("/goods/save_or_update", methods=["POST"])
@login_required
def save_or_update_goods():
    req = GoodsSaveOrUpdateRequest(ImmutableMultiDict(request.values))

    if req.validate():
        return HttpResponseUtil.success(GoodsService.save_or_update_goods(req))
    else:
        return HttpResponseUtil.param_error(req.errors)


@route_admin.route("/goods/<goods_id>", methods=["POST"])
def get_goods_by_id(goods_id):
    return HttpResponseUtil.success(GoodsService.get_goods_detail(goods_id))


@route_admin.route("/goods/operate", methods=["POST"])
@login_required
def operate_goods():
    req = GoodsOperateRequest(ImmutableMultiDict(request.json))
    if req.validate():
        return HttpResponseUtil.success(GoodsService.operate_goods(req))
    else:
        return HttpResponseUtil.param_error(req.errors)


@route_admin.route("/goods/modify_stock", methods=["POST"])
@login_required
def modify_goods_stock():
    req = GoodsStockModifyRequest(ImmutableMultiDict(request.json))
    if req.validate():
        return HttpResponseUtil.success(GoodsService.modify_goods_stock(req))
    else:
        return HttpResponseUtil.param_error(req.errors)
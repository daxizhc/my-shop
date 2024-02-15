from www import route_index
from service.GoodsService import GoodsService
from utils.HttpResponseUtil import HttpResponseUtil


@route_index.route("/goods/detail/<goods_id>")
def goods_detail(goods_id):
    goods = GoodsService.get_goods_detail(goods_id)
    return HttpResponseUtil.success(goods)

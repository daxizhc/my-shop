from flask import request

from application import app
from enums.GoodsEnum import GoodsStatusEnum
from model.IndexBanner import IndexBanner
from service.CategoryService import CategoryService
from service.GoodsService import GoodsService
from utils.HttpResponseUtil import HttpResponseUtil
from www import route_index


@route_index.route("/banners")
def banners():
    index_banners = IndexBanner.query.filter_by(is_deleted=0).all()

    result_list = []
    for banner in index_banners:
        result_list.append({
            "image": banner.image
        })

    return HttpResponseUtil.success(result_list)


@route_index.route("/goods_list")
def goods_list():
    """
    获取商品列表
    :return: 商品列表
    """
    req = request.values
    start_index = int(req['start_index']) if 'start_index' in req else 0
    page_size = app.config['INDEX_PAGE_SIZE']
    search_key = str(req['search_key']) if 'search_key' in req else ''
    category_id = int(req['category_id']) if 'category_id' in req else 0
    category_ids = [category_id] if category_id > 0 else None

    result = {'has_next': False, 'goods_list': []}
    count = GoodsService.get_goods_count(search_key, GoodsStatusEnum.ON_SALE.value, category_ids)

    if start_index >= count:
        return HttpResponseUtil.success(result)

    if start_index + page_size < count:
        result['has_next'] = True

    goods_items = GoodsService.get_goods_list(start_index, page_size, search_key,
                                              GoodsStatusEnum.ON_SALE.value, category_ids)
    result_goods_list = []
    for goods_item in goods_items:
        result_goods_list.append({
            "id": goods_item.id,
            "item_name": goods_item.item_name,
            "item_price": str(goods_item.item_price),
            "main_image": goods_item.main_image
        })
    result['goods_list'] = result_goods_list

    return HttpResponseUtil.success(result)


@route_index.route("/category_list")
def get_category_list():
    """
    获取商品分类列表
    :return: 商品分类列表
    """

    category_list = CategoryService.get_category_list(True)

    result_list = []
    for category in category_list:
        result_list.append({
            "id": category.id,
            "category_name": category.category_name
        })

    return HttpResponseUtil.success(result_list)

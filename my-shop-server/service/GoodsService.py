from sqlalchemy import and_

from application import db
from enums.GoodsEnum import GoodsOperateEnum
from exception.CommonException import GOODS_NOT_EXIST, GOODS_IS_ON_SALE, GOODS_STOCK_NOT_ENOUGH
from model.GoodsImage import GoodsImage
from model.GoodsItem import GoodsItem
from vo.web.response.PageResponse import build_page_response


class GoodsService:

    @staticmethod
    def get_goods_count(search_key, status, category_ids=None):
        query = GoodsItem.query.filter(and_(GoodsItem.is_deleted == 0,
                                            GoodsItem.item_name.like('%{0}%'.format(search_key))))
        if category_ids:
            query = query.filter(GoodsItem.category_id.in_(category_ids))
        if status is not None:
            query = query.filter_by(status=status)

        return query.count()

    @staticmethod
    def get_goods_list(start_index, page_size, search_key, status, category_ids=None):
        query = GoodsItem.query.filter(and_(GoodsItem.is_deleted == 0,
                                            GoodsItem.item_name.like('%{0}%'.format(str(search_key)))))
        if category_ids:
            query = query.filter(GoodsItem.category_id.in_(category_ids))
        if status is not None:
            query = query.filter_by(status=status)

        return query.order_by(GoodsItem.id.desc()).offset(start_index).limit(page_size).all()

    @staticmethod
    def get_goods_detail(goods_id):
        goods = GoodsItem.query.filter(and_(GoodsItem.is_deleted == 0, GoodsItem.id == goods_id)).first()

        result = None
        if goods:
            result = {
                'id': goods.id,
                'item_name': goods.item_name,
                'item_price': str(goods.item_price),
                'item_desc': goods.item_desc,
                'item_stock': goods.item_stock,
                'goods_images': [goods.main_image],
                'main_image': goods.main_image,
                'category_id': goods.category_id,
            }
            goods_image = GoodsImage.query.filter_by(goods_id=goods_id, is_deleted=0).all()
            if len(goods_image) > 0:
                for image in goods_image:
                    result['goods_images'].append(image.image_url)

        return result

    @classmethod
    def get_goods_page(cls, request):
        search_key = request.search_key.data
        page_number = request.page_number.data
        page_size = request.page_size.data
        category_ids = request.category_ids
        status = request.status
        goods_count = cls.get_goods_count(search_key=search_key, status=status, category_ids=category_ids)
        if goods_count == 0:
            return build_page_response([], page_number, page_size, goods_count)

        goods_list = cls.get_goods_list((page_number - 1) * page_size, page_size, search_key,
                                        status=status, category_ids=category_ids)

        result_list = []
        for goods in goods_list:
            result_list.append({
                'id': goods.id,
                'item_name': goods.item_name,
                'item_price': str(goods.item_price),
                'item_desc': goods.item_desc,
                'item_stock': goods.item_stock,
                'main_image': goods.main_image,
                'status': goods.status
            })

        return build_page_response(result_list, page_number, page_size, goods_count)

    @classmethod
    def save_or_update_goods(cls, request):
        goods_id = request.id.data
        if goods_id:
            goods_item = GoodsItem.query.get(goods_id)
            if not goods_item:
                raise GOODS_NOT_EXIST
            goods_item.category_id = request.category_id.data
            goods_item.item_name = request.item_name.data
            goods_item.main_image = request.main_image.data
            goods_item.item_desc = request.item_desc.data
            goods_item.item_price = request.item_price.data
            db.session.add(goods_item)
            db.session.commit()
            return None
        else:
            goods_item = GoodsItem(request.data)
            db.session.add(goods_item)
            db.session.commit()
            return None

    @classmethod
    def operate_goods(cls, request):
        goods_id = request.id.data
        goods_item = GoodsItem.query.filter_by(id=goods_id, is_deleted=0).first()
        if not goods_item:
            raise GOODS_NOT_EXIST

        operate_type = request.operate_type.data
        if operate_type == GoodsOperateEnum.DELETED.value:
            if goods_item.status == GoodsOperateEnum.ON_SALE.value:
                raise GOODS_IS_ON_SALE
            goods_item.is_deleted = 1
        elif operate_type == GoodsOperateEnum.ON_SALE.value:
            goods_item.status = GoodsOperateEnum.ON_SALE.value
        elif operate_type == GoodsOperateEnum.OFF_SALE.value:
            goods_item.status = GoodsOperateEnum.OFF_SALE.value

        db.session.add(goods_item)
        db.session.commit()

        return None

    @classmethod
    def modify_goods_stock(cls, request):
        goods_id = request.id.data
        goods_item = GoodsItem.query.filter_by(id=goods_id, is_deleted=0).first()
        if not goods_item:
            raise GOODS_NOT_EXIST

        new_stock = goods_item.item_stock + request.stock_change.data
        if new_stock < 0:
            raise GOODS_STOCK_NOT_ENOUGH

        goods_item.item_stock = new_stock
        db.session.add(goods_item)
        db.session.commit()

        return None


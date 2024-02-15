from exception.CommonException import CATEGORY_NOT_EXIST
from model.GoodsCategory import GoodsCategory
from sqlalchemy import and_
from enums.CategoryEnum import CategoryOperateEnum
from application import db


class CategoryService:

    @staticmethod
    def get_category_list(valid=None):
        if valid:
            return (GoodsCategory.query.filter(and_(GoodsCategory.is_deleted == 0, GoodsCategory.status == 1))
                    .limit(100).all())
        else:
            return GoodsCategory.query.filter_by(is_deleted=0).limit(100).all()

    @classmethod
    def save_or_update_category(cls, request):
        category_id = request.id.data
        if category_id:
            category = cls.get_or_raise_by_id(category_id)
            category.category_name = request.category_name.data
            category.weight = request.weight.data
            db.session.add(category)
            db.session.commit()
        else:
            category = GoodsCategory()
            category.category_name = request.category_name.data
            category.weight = request.weight.data
            category.status = 0
            category.is_deleted = 0
            db.session.add(category)
            db.session.flush()
            category_id = category.id
            db.session.commit()
        return category_id

    @classmethod
    def get_or_raise_by_id(cls, category_id):
        category = GoodsCategory.query.filter_by(id=category_id).first()
        if not category:
            raise CATEGORY_NOT_EXIST
        return category

    @classmethod
    def operate_category(cls, request):
        category_id = request.id.data
        category = cls.get_or_raise_by_id(category_id)
        operate = request.operate.data
        if CategoryOperateEnum.DELETED.value == operate:
            category.is_deleted = 1
        elif CategoryOperateEnum.INACTIVE.value == operate:
            category.status = 0
        elif CategoryOperateEnum.ACTIVE.value == operate:
            category.status = 1
        db.session.add(category)
        db.session.commit()

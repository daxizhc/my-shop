# coding: utf-8
from application import db


class GoodsItem(db.Model):
    __tablename__ = 'goods_item'

    id = db.Column(db.BigInteger, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='商品名称')
    item_price = db.Column(db.Numeric(10, 2), nullable=False, server_default=db.FetchedValue(), info='售卖金额')
    main_image = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='主图')
    item_desc = db.Column(db.String(10000), nullable=False, server_default=db.FetchedValue(), info='描述')
    item_stock = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='库存量')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='状态 1：有效 0：无效')
    category_id = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue(), info='分类id')
    is_deleted = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(),
                           info='是否删除，(0：正常，1：已删除)')
    create_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')
    creator = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='创建人')
    updater = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='更新人')

    def __init__(self, attrs):
        for k, v in attrs.items():
            if hasattr(self, k):
                setattr(self, k, v)

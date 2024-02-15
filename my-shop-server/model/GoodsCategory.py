# coding: utf-8
from application import db


class GoodsCategory(db.Model):
    __tablename__ = 'goods_category'

    id = db.Column(db.BigInteger, primary_key=True)
    category_name = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='类目名称')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='状态 1：展示 0：隐藏')
    weight = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='权重')
    is_deleted = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(),
                           info='是否删除，(0：正常，1：已删除)')
    create_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')
    creator = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='创建人')
    updater = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='更新人')

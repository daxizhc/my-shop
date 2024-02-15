# coding: utf-8
from application import db


class GoodsImage(db.Model):
    __tablename__ = 'goods_image'

    id = db.Column(db.BigInteger, primary_key=True)
    goods_id = db.Column(db.BigInteger, nullable=False, info='商品id')
    image_url = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='图片url')
    image_type = db.Column(db.Integer, nullable=False, info='类型，1：商品图、2：介绍图')
    is_deleted = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(),
                           info='是否删除，(0：正常，1：已删除)')
    create_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')
    creator = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='创建人')
    updater = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='更新人')

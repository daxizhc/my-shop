# coding: utf-8
from application import db


class OrderInfo(db.Model):
    __tablename__ = 'order_info'

    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, nullable=False, info='userId')
    item_name = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='商品名称')
    item_price = db.Column(db.Numeric(10, 2), nullable=False, server_default=db.FetchedValue(), info='售卖金额')
    item_image = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='主图')
    item_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='数量')
    remark = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='备注')
    address_name = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue(), info='收货人姓名')
    address_mobile = db.Column(db.String(11), nullable=False, server_default=db.FetchedValue(), info='收货人手机号码')
    address_detail = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='收货地址')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='状态 ')
    is_deleted = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(),
                           info='是否删除，(0：正常，1：已删除)')
    create_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')
    creator = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='创建人')
    updater = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='更新人')

    def build_info(self):
        return {
            'id': self.id,
            'item_name': self.item_name,
            'item_price': str(self.item_price),
            'item_image': self.item_image,
            'item_count': self.item_count,
            'remark': self.remark,
            'address_name': self.address_name,
            'address_mobile': self.address_mobile,
            'address_detail': self.address_detail,
            'status': self.status,
            'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S'),
        }

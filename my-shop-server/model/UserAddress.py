# coding: utf-8
from application import db


class UserAddress(db.Model):

    __tablename__ = 'user_address'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False, info='用户id')
    nickname = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue(), info='收货人姓名')
    mobile = db.Column(db.String(11), nullable=False, server_default=db.FetchedValue(), info='收货人手机号码')
    province_str = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='省名称')
    city_str = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='市名称')
    county_str = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='区域名称')
    street_str = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='街道名称')
    address = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='详细地址')
    is_default = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='默认地址')
    is_deleted = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(),
                           info='是否删除，(0：正常，1：已删除)')
    create_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')
    creator = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='创建人')
    updater = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='更新人')

    def build_simple_info(self):
        return {
            'id': self.id,
            'nickname': self.nickname,
            'mobile': self.mobile,
            'province_str': self.province_str,
            'city_str': self.city_str,
            'country_str': self.county_str,
            'street_str': self.street_str,
            'is_default': self.is_default,
            'address': self.address,
            'detail': self.province_str + self.city_str + self.county_str + self.street_str + self.address
        }

    @property
    def detail(self):
        return self.province_str + self.city_str + self.county_str + self.street_str + self.address


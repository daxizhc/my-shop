from flask import g

from application import db
from exception.CommonException import ADDRESS_NOT_EXIST
from model.UserAddress import UserAddress
from service.UserService import UserService


class AddressService:

    @staticmethod
    def query_default_address(user_id):
        return UserAddress.query.filter_by(user_id=user_id, is_default=1, is_deleted=0).first()

    @staticmethod
    def query_address_list(user_id):
        return UserAddress.query.filter_by(user_id=user_id, is_deleted=0).all()

    @staticmethod
    def query_address(user_id, address_id):
        return UserAddress.query.filter_by(user_id=user_id, id=address_id, is_deleted=0).first()

    @classmethod
    def save_or_update_address(cls, req):
        openid = g.current_openid
        user = UserService.query_by_openid(openid)
        user_id = user.id
        address_id = req.id.data

        if address_id:
            address_info = cls.query_address(user_id, address_id)
            if not address_info:
                raise ADDRESS_NOT_EXIST
        else:
            address_info = UserAddress()
            address_info.user_id = user_id

        address_info.nickname = req.nickname.data
        address_info.mobile = req.mobile.data
        address_info.province_str = req.province_str.data
        address_info.city_str = req.city_str.data
        address_info.county_str = req.country_str.data
        address_info.address = req.address.data

        db.session.add(address_info)
        db.session.commit()

        return True

    @classmethod
    def delete_address(cls, req):
        openid = g.current_openid
        user = UserService.query_by_openid(openid)
        user_id = user.id
        address_id = req.id.data

        address_info = cls.query_address(user_id, address_id)
        if not address_info:
            raise ADDRESS_NOT_EXIST
        address_info.is_deleted = 1

        db.session.add(address_info)
        db.session.commit()



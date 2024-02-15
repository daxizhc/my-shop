from application import app, db
from flask import g
import requests
from model.UserInfo import UserInfo
from utils.CipherUtil import AESClassicCipher

from exception.CommonException import THIRD_PARTY_ERROR, USER_NOT_EXIST

WECHAT_LOGIN_URL = "https://api.weixin.qq.com/sns/jscode2session"


class UserService:

    @classmethod
    def login(cls, code):
        params = {
            "appid": app.config['APP_ID'],
            "secret": app.config['APP_SECRET'],
            "js_code": code,
            "grant_type": "authorization_code"
        }

        response = requests.get(WECHAT_LOGIN_URL, params=params)
        data = response.json()

        if 'errcode' in data and data['errcode'] != 0:
            raise THIRD_PARTY_ERROR

        openid = cls.register_if_not_exist(data)

        return cls.generate_user_token(openid)

    @classmethod
    def register_if_not_exist(cls, data):
        """
        如果用户不存在，则注册
        :param data: 包括openid、session_key
        :return: openid
        """
        user_info = UserInfo.query.filter_by(openid=data['openid']).first()
        if user_info is None:
            user_info = UserInfo()
            user_info.openid = data['openid']
            user_info.session_key = data['session_key']
            db.session.add(user_info)
            db.session.commit()
        return user_info.openid

    @staticmethod
    def generate_user_token(openid):
        return AESClassicCipher(app.config['CIPHER_SECRET']).encrypt(openid)

    @staticmethod
    def query_by_openid(openid):
        return UserInfo.query.filter_by(openid=openid, is_deleted=0).first()

    @staticmethod
    def query_user_info():
        openid = g.current_openid
        user = UserService.query_by_openid(openid)
        if not user:
            raise USER_NOT_EXIST
        return user

    @classmethod
    def update_user_info(cls, request):
        user_info = cls.query_user_info()
        if not request.avatar.data and not request.nickname.data:
            return
        if request.avatar.data:
            user_info.avatar = request.avatar.data
        if request.nickname.data:
            user_info.nickname = request.nickname.data

        db.session.add(user_info)
        db.session.commit()



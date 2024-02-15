# coding: utf-8
from application import db


class UserInfo(db.Model):
    __tablename__ = 'user_info'

    id = db.Column(db.BigInteger, primary_key=True)
    openid = db.Column(db.String(100), nullable=False, info='openid')
    session_key = db.Column(db.String(255), nullable=False, info='session_key')
    avatar = db.Column(db.String(255), info='头像')
    nickname = db.Column(db.String(255), info='昵称')
    is_deleted = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(),
                           info='是否删除，(0：正常，1：已删除)')
    create_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')
    creator = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='创建人')
    updater = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='更新人')

    def build_info(self):
        return {
            'id': self.id,
            'avatar': self.avatar,
            'nickname': self.nickname,
            'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S'),
        }

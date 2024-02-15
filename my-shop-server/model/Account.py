# coding: utf-8
from flask_login import UserMixin

from application import db


class Account(db.Model, UserMixin):
    __tablename__ = 'account'

    id = db.Column(db.BigInteger, primary_key=True)
    mobile = db.Column(db.String(100), nullable=False, info='mobile')
    password = db.Column(db.String(255), nullable=False, info='密码')
    avatar = db.Column(db.String(255), info='头像')
    nickname = db.Column(db.String(255), info='昵称')
    is_deleted = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(),
                           info='是否删除，(0：正常，1：已删除)')
    create_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')
    creator = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='创建人')
    updater = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue(), info='更新人')

    def get_id(self):
        return self.id

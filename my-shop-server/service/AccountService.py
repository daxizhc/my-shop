import flask
from flask_login import login_user
from application import login_manager

from exception.CommonException import ACCOUNT_NOT_EXIST, ACCOUNT_PASSWORD_ERROR
from model.Account import Account


class AccountService:

    @staticmethod
    def account_login(req):
        mobile = req.mobile.data
        password = req.password.data

        account_info = Account.query.filter_by(mobile=mobile, is_deleted=0).first()
        if not account_info:
            raise ACCOUNT_NOT_EXIST
        if account_info.password != password:
            raise ACCOUNT_PASSWORD_ERROR

        login_user(account_info)

        next_url = flask.request.args.get('next')

        return flask.redirect(next_url or flask.url_for('route_admin.index'))



    @staticmethod
    @login_manager.user_loader
    def load_user(user_id):
        return Account.query.filter_by(id=user_id, is_deleted=0).first()
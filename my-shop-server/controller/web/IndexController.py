from flask import render_template, redirect, url_for
from flask import request
from flask_login import login_required, logout_user
from werkzeug.datastructures import ImmutableMultiDict
from service.AccountService import AccountService

from utils.HttpResponseUtil import HttpResponseUtil
from vo.web.request.AccountRequest import AccountLoginRequest
from www import route_admin


@route_admin.route("/")
@login_required
def index():
    return render_template("index.html")



@route_admin.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    req = AccountLoginRequest(ImmutableMultiDict(request.form))
    if req.validate():
        return AccountService.account_login(req)
    else:
        return HttpResponseUtil.param_error(req.errors)


@route_admin.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('route_admin.login'))

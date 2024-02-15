from flask import request
from werkzeug.datastructures import ImmutableMultiDict

from service.UserService import UserService
from vo.api.request.UserRequest import UpdateUserRequest
from www import route_index
from utils.HttpResponseUtil import HttpResponseUtil


@route_index.route("/user/login", methods=['POST'])
def login():
    code = request.json['code']
    token = UserService.login(code)
    return HttpResponseUtil.success(token)


@route_index.route("/user/info", methods=['POST'])
def user_info():
    return HttpResponseUtil.success(UserService.query_user_info().build_info())


@route_index.route("/user/update", methods=['POST'])
def update_user_info():
    req = UpdateUserRequest(ImmutableMultiDict(request.json))
    UserService.update_user_info(req)
    return HttpResponseUtil.success(True)

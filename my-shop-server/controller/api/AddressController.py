from flask import g, request
from werkzeug.datastructures import ImmutableMultiDict

from utils.HttpResponseUtil import HttpResponseUtil
from vo.api.request.AddressRequest import SaveOrUpdateAddressRequest, DeleteAddressRequest
from www import route_index
from service.UserService import UserService
from service.AddressService import AddressService


@route_index.route("/address/default", methods=["POST"])
def default_address():
    openid = g.current_openid
    user = UserService.query_by_openid(openid)
    address = AddressService.query_default_address(user.id)
    return HttpResponseUtil.success(address.build_simple_info())


@route_index.route("/address/list", methods=["POST"])
def address_list():
    openid = g.current_openid
    user = UserService.query_by_openid(openid)

    addresses = AddressService.query_address_list(user.id)

    result = []
    for address in addresses:
        result.append(address.build_simple_info())
    return HttpResponseUtil.success(result)


@route_index.route("/address/info", methods=["POST"])
def address_info():
    openid = g.current_openid
    user = UserService.query_by_openid(openid)
    address_id = request.json['address_id']
    address = AddressService.query_address(user.id, address_id)
    return HttpResponseUtil.success(address.build_simple_info())


@route_index.route("/address/save_or_update", methods=["POST"])
def save_or_update_address():
    req = SaveOrUpdateAddressRequest(ImmutableMultiDict(request.json))
    if req.validate():
        return HttpResponseUtil.success(AddressService.save_or_update_address(req))
    else:
        return HttpResponseUtil.param_error(req.errors)


@route_index.route("/address/delete", methods=["POST"])
def delete_address():
    req = DeleteAddressRequest(ImmutableMultiDict(request.json))
    if req.validate():
        return HttpResponseUtil.success(AddressService.delete_address(req))
    else:
        return HttpResponseUtil.param_error(req.errors)




from flask_login import login_required
from werkzeug.datastructures import ImmutableMultiDict

from service.CategoryService import CategoryService
from utils.HttpResponseUtil import HttpResponseUtil
from www import route_admin
from flask import render_template, request
from vo.web.request.CategoryRequest import SaveOrUpdateCategoryRequest, OperateCategoryRequest


# 设置其他目录为静态目录
@route_admin.route("/goods/<path:filename>")
def category_page(filename):
    return render_template('/goods/' + filename)


@route_admin.route("/category/list")
@login_required
def query_category_list():
    category_list = CategoryService.get_category_list()
    result_list = []
    for category in category_list:
        result_list.append({
            "id": category.id,
            "name": category.category_name,
            "weight": category.weight,
            "status": 'checked' if category.status == 1 else '',
        })
    return HttpResponseUtil.success(result_list)


@route_admin.route("/category/save_or_update", methods=["POST"])
@login_required
def save_or_update_category():
    req = SaveOrUpdateCategoryRequest(ImmutableMultiDict(request.json))
    return HttpResponseUtil.success(CategoryService.save_or_update_category(req))


@route_admin.route("/category/operate", methods=["POST"])
@login_required
def operate_category():
    req = OperateCategoryRequest(ImmutableMultiDict(request.json))
    if req.validate():
        CategoryService.operate_category(req)
        return HttpResponseUtil.success()
    else:
        return HttpResponseUtil.fail(400, req.errors)



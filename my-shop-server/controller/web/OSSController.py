from www import route_admin
from flask import request
import oss2, time
from utils.HttpResponseUtil import HttpResponseUtil


@route_admin.route("/oss/upload_image", methods=["POST"])
def upload_image():
    file = request.files['file']
    if file:
        return HttpResponseUtil.success(upload_img_to_oss(file))
    return HttpResponseUtil.fail(400, 'file is empty')


def upload_img_to_oss(file):
    auth = oss2.Auth('阿里云oss', '阿里云oss')
    bucket = oss2.Bucket(auth, '阿里云oss', '阿里云oss')
    new_article_img_name = 'goods_image/' + str(int(round(time.time() * 1000))) + '.png'
    resp = bucket.put_object(new_article_img_name, file).resp
    return resp.response.url

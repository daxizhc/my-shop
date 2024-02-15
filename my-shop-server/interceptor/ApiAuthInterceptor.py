from flask import request, g

from application import app
from exception.CommonException import USER_NOT_LOGIN
from utils.CipherUtil import AESClassicCipher


@app.before_request
def before_request():
    path = request.path
    if not path.startswith("/api") or path.startswith("/api/user/login"):
        return
    token = request.headers.get("token")
    if token is None:
        raise USER_NOT_LOGIN

    openid = AESClassicCipher(app.config['CIPHER_SECRET']).decrypt(token)
    g.current_openid = openid





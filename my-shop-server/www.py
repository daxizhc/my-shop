from application import app
from flask import Blueprint

route_index = Blueprint('index_app', __name__)

from controller.api.IndexController import *
from controller.api.GoodsController import *
from controller.api.UserController import *
from controller.api.AddressController import *
from controller.api.OrderController import *

from interceptor.ApiAuthInterceptor import *

app.register_blueprint(route_index, url_prefix="/api")

route_admin = Blueprint('route_admin', __name__)
from controller.web.IndexController import *
from controller.web.CategoryController import *
from controller.web.GoodsController import *
from controller.web.OrderController import *
from controller.web.OSSController import *

app.register_blueprint(route_admin, url_prefix="/admin")

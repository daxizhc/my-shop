from flask import Flask
from flask_script import Manager
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


class Application(Flask):

    def __init__(self, import_name):
        super(Application, self).__init__(import_name, static_folder="static", static_url_path="/")
        self.config.from_pyfile("config/base_setting.py")
        db.init_app(self)


db = SQLAlchemy()
app = Application(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
manager = Manager(app)
login_manager = LoginManager(app)
login_manager.login_view = "route_admin.login"


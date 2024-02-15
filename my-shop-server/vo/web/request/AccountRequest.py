from wtforms import Form, StringField
from wtforms.validators import InputRequired


class AccountLoginRequest(Form):
    mobile = StringField(validators=[InputRequired(message="请输入手机号")])
    password = StringField(validators=[InputRequired(message="请输入密码")])
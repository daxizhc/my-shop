from wtforms import Form, StringField, IntegerField
from wtforms.validators import InputRequired


class SaveOrUpdateAddressRequest(Form):
    id = IntegerField()
    nickname = StringField(validators=[InputRequired(message="请输入收件人姓名")])
    mobile = StringField(validators=[InputRequired(message="请输入收件人手机号")])
    province_str = StringField(validators=[InputRequired(message="请输入省份")])
    city_str = StringField(validators=[InputRequired(message="请输入城市")])
    country_str = StringField(validators=[InputRequired(message="请输入区域")])
    address = StringField(validators=[InputRequired(message="请输入详细地址")])


class DeleteAddressRequest(Form):
    id = IntegerField(validators=[InputRequired(message="请输入地址id")])



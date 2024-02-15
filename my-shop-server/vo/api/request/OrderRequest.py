from wtforms import Form, StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange


class CreateOrderRequest(Form):
    item_id = IntegerField(validators=[InputRequired(message="请输入商品id")])
    item_count = IntegerField(validators=[InputRequired(message="请输入商品数量")])
    remark = StringField()
    address_id = IntegerField(validators=[InputRequired(message="请输入地址id")])


class OperateOrderRequest(Form):
    id = IntegerField(validators=[InputRequired(message="请输入订单id")])
    operate = IntegerField(validators=[InputRequired(message="请输入操作类型")])


class QueryOrderRequest(Form):
    status = IntegerField()
    start_id = IntegerField(validators=[InputRequired(message="请输入起始id")])
    page_size = IntegerField(validators=[InputRequired(message="请输入每页数量"), NumberRange(min=1, max=20)])

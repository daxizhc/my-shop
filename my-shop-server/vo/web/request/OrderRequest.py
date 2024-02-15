from wtforms import Form, IntegerField
from wtforms.validators import NumberRange, InputRequired


class OrderPageQueryRequest(Form):
    status = IntegerField()
    page_number = IntegerField(validators=[NumberRange(min=1)])
    page_size = IntegerField(validators=[NumberRange(min=1, max=50)])


class OperateOrderRequest(Form):
    id = IntegerField(validators=[InputRequired(message="请输入订单id")])
    operate = IntegerField()


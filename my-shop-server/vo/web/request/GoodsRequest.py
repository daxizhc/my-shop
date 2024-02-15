from wtforms import Form, StringField, IntegerField, DecimalField
from wtforms.validators import Length, NumberRange, Optional, Required


class GoodsPageQueryRequest(Form):
    search_key = StringField(validators=[Length(min=0, max=20)])
    page_number = IntegerField(validators=[NumberRange(min=1)])
    page_size = IntegerField(validators=[NumberRange(min=1, max=50)])


class GoodsSaveOrUpdateRequest(Form):
    id = IntegerField(validators=[Optional(), NumberRange(min=1)])
    item_name = StringField(validators=[Length(min=1, max=20)])
    category_id = IntegerField(validators=[NumberRange(min=1)])
    item_price = DecimalField(validators=[NumberRange(min=1)])
    main_image = StringField(validators=[Length(min=0, max=200)])
    item_desc = StringField(validators=[Length(min=0, max=200)])


class GoodsOperateRequest(Form):
    id = IntegerField(validators=[Optional(), NumberRange(min=1)])
    operate_type = IntegerField(validators=[NumberRange(min=-1, max=1)])


class GoodsStockModifyRequest(Form):
    id = IntegerField(validators=[NumberRange(min=1)])
    stock_change = IntegerField(validators=[Required()])

from wtforms import Form, StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange


class SaveOrUpdateCategoryRequest(Form):
    id = IntegerField()
    category_name = StringField(validators=[InputRequired(message="请输入分类名称")])
    weight = IntegerField()


class OperateCategoryRequest(Form):
    id = IntegerField(validators=[InputRequired(message="请输入分类id")])
    operate = IntegerField(validators=[NumberRange(min=-1, max=1)])
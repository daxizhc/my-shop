from wtforms import Form, StringField


class UpdateUserRequest(Form):
    nickname = StringField()
    avatar = StringField()
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class SendLink(Form):
    openid = StringField('threadlink', validators=[DataRequired()])
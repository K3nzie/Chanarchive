from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class SendLink(Form):
    link = StringField('threadlink', validators=[DataRequired()])

#def getJson(link):

 # 	f = request_files['thread.json']
 # 	f.save('jsons_files/' + secure_filename(f))


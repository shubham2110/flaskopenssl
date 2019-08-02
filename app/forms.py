from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length
from flask import flash


class SignCertFrom(FlaskForm):
	cakey = StringField('cakey')
	cacert = StringField('cacert')
	csr = TextAreaField('csr',validators=[DataRequired()])
	days = StringField('days')
	submit = SubmitField('Get Cert')

	

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField,PasswordField,BooleanField, SelectField

from wtforms.validators import DataRequired, Length


class ToDO(FlaskForm):
    name = StringField('Title',validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    status = SelectField('Status', choices=[('New', 'New'),
                                                 ('In Progress', 'Progress'), ('Closed', 'Closed') ])
    submit = SubmitField('Submit')



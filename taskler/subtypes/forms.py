from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class SubtypeForm(FlaskForm):
    type = StringField('Type',
                       validators=[DataRequired(), Length(max=50)],
                       render_kw={'placeholder': 'Enter type...'})
    submit = SubmitField('Create Subtype')

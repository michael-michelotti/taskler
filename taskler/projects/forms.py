import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, Length, Optional
from wtforms.fields.html5 import DateTimeLocalField


class ProjectForm(FlaskForm):
    title = StringField('Title',
                        validators=[DataRequired(), Length(max=50)],
                        render_kw={'placeholder': 'Enter title...'})
    description = TextAreaField('Description',
                                validators=[DataRequired(), Length(max=300)],
                                render_kw={'placeholder': 'Enter description...'})
    start_date = DateTimeLocalField('Start Date',
                                    default=datetime.datetime.now(),
                                    format='%Y-%m-%dT%H:%M',
                                    validators=[Optional()])
    end_date = DateTimeLocalField('End Date',
                                  format='%Y-%m-%dT%H:%M',
                                  validators=[Optional()])
    status = SelectField('Status Upon Creation',
                         choices=['Created', 'In Work', 'Complete', 'On Hold'],
                         # need to export these options somewhere
                         validators=[DataRequired()])
    submit = SubmitField('Create Project')

import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DateTimeField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, Length, Optional


class ProjectForm(FlaskForm):
    title = StringField('Title',
                        validators=[DataRequired(), Length(max=50)],
                        render_kw={'placeholder': 'Enter title...'})
    description = TextAreaField('Description',
                                validators=[DataRequired(), Length(max=300)],
                                render_kw={'placeholder': 'Enter description...'})
    start_date = DateTimeField('Start Date',
                               default=datetime.datetime.now(),
                               format='%m/%d/%Y',
                               validators=[Optional()])
    end_date = DateTimeField('End Date',
                             format='%m/%d/%Y',
                             validators=[Optional()])
    status = SelectField('Status Upon Creation',
                         choices=['Created', 'In Work', 'Complete', 'On Hold'],
                         # need to export these options somewhere
                         validators=[DataRequired()])
    submit = SubmitField('Create Project')

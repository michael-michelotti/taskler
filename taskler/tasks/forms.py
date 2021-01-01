import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, SelectMultipleField
from wtforms.fields.html5 import DateTimeLocalField
from wtforms.validators import DataRequired, Length, Optional

from taskler.db import db_session
from taskler.models import Project, Subtype


def fetch_all_titles(session, model):
    all_models = session.query(model).all()
    return [model.title for model in all_models]


def fetch_all_types(session, model):
    all_models = session.query(model).all()
    return [(model.type, model.type) for model in all_models]


class TaskForm(FlaskForm):
    title = StringField('Title',
                        validators=[DataRequired(), Length(max=50)],
                        render_kw={'placeholder': 'Enter title...'})
    description = TextAreaField('Description',
                                validators=[DataRequired(), Length(max=300)],
                                render_kw={'placeholder': 'Enter description...'})
    start_date = DateTimeLocalField('Start Date',
                                    default=datetime.datetime.now(),
                                    validators=[Optional()],
                                    format='%Y-%m-%dT%H:%M')
    date_due = DateTimeLocalField('Due Date',
                                  validators=[Optional()],
                                  format='%Y-%m-%dT%H:%M')
    project_name = SelectField('Parent Project',
                               choices=fetch_all_titles(db_session, Project),
                               validators=[Optional()])
    status = SelectField('Status Upon Creation',
                         choices=['Created', 'In Work', 'Complete', 'On Hold'],  # need to export these options somewhere
                         validators=[DataRequired()])
    subtypes = SelectMultipleField('Subtypes (select all applicable)',
                                   choices=fetch_all_types(db_session, Subtype))
    submit = SubmitField('Create Task')

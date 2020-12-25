from flask import Blueprint, flash, redirect, url_for, render_template
from taskler.subtypes.forms import SubtypeForm
from taskler.db import db_session
from taskler.models import Subtype


subtypes = Blueprint('subtypes', __name__)


@subtypes.route('/subtype/new', methods=['GET', 'POST'])
def new_subtype():
    form = SubtypeForm()
    my_subtypes = db_session.query(Subtype).all()
    if form.validate_on_submit():
        my_subtype = Subtype(type=form.type.data)
        db_session.add(my_subtype)
        db_session.commit()
        flash('You have successfully created a subtype. You can apply it to a task', 'success')
        return redirect(url_for('subtypes.all_subtypes'))
    return render_template('subtypes/create_subtype.html', form=form, subtypes=my_subtypes)


@subtypes.route('/subtype/all')
def all_subtypes():
    my_subtypes = db_session.query(Subtype).all()
    return render_template('subtypes/all_subtypes.html', subtypes=my_subtypes)

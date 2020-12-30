from flask import Blueprint, flash, redirect, url_for, render_template, request
from taskler.models import Task
from taskler.tasks.forms import TaskForm
from taskler.db import db_session, init_db
from taskler.models import Project, Subtype


tasks = Blueprint('tasks', __name__)


@tasks.route('/task/new', methods=['GET', 'POST'])
def new_task():
    form = TaskForm()
    if form.validate_on_submit():
        project_id = db_session.query(Project).filter(Project.title == form.project_name.data).first().id
        my_task = Task(title=form.title.data,
                       description=form.description.data,
                       date_due=form.date_due.data,
                       status=form.status.data,
                       project_id=project_id)
        task_subtypes = []
        for subtype in form.subtypes.data:
            task_subtypes.append(db_session.query(Subtype).filter(Subtype.type == subtype).first())
        my_task.subtypes = task_subtypes
        db_session.add(my_task)
        db_session.commit()
        flash('Your task has been created!', 'success')
        return redirect(url_for('tasks.task', task_id=my_task.id))
    return render_template('tasks/create_task.html', form=form)


@tasks.route('/task/all')
def all_tasks():
    my_tasks = db_session.query(Task).all()
    return render_template('tasks/all_tasks.html', tasks=my_tasks)


@tasks.route('/task/<int:task_id>')
def task(task_id):
    init_db()
    my_task = db_session.query(Task).get(task_id)
    return render_template('tasks/task.html', task=my_task)


@tasks.route('/task/<int:task_id>/update', methods=['GET', 'POST'])
def update_task(task_id):
    my_task = db_session.query(Task).get(task_id)
    form = TaskForm()
    if form.validate_on_submit():
        new_project = db_session.query(Project).filter_by(title=form.project_name.data).first()
        my_task.title = form.title.data
        my_task.description = form.description.data
        my_task.date_due = form.date_due.data
        my_task.project = new_project
        my_task.status = form.status.data
        # my_task.subtypes = form.subtypes.data
        db_session.commit()
        flash('Your task has successfully updated', 'success')
        redirect(url_for('main.home'))
    elif request.method == 'GET':
        form.title.data = my_task.title
        form.description.data = my_task.description
        form.date_due.data = my_task.date_due
        form.project_name.data = my_task.project.title
        form.status.data = my_task.status
        form.subtypes.data = my_task.subtypes
    return render_template('tasks/create_task.html', title='Update Task', form=form)


@tasks.route('/task/<int:task_id>/delete', methods=['GET', 'POST'])
def delete_task(task_id):
    my_task = db_session.query(Task).get(task_id)
    if my_task:
        project_id = my_task.project.id
        db_session.delete(my_task)
        db_session.commit()
        flash('Your task has been deleted!', 'success')
        return redirect(url_for('projects.project', project_id=project_id))
    flash('Task deletion failed', 'danger')
    return render_template(url_for('main.home'))

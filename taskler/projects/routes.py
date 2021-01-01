from flask import render_template, Blueprint, flash, redirect, url_for, request
from taskler.models import Project, Task, Subtype
from taskler.db import db_session
from taskler.projects.forms import ProjectForm
from taskler.tasks.forms import TaskForm
from taskler.utils import local_to_utc


projects = Blueprint('projects', __name__)


@projects.route('/project/new', methods=['GET', 'POST'])
def new_project():
    form = ProjectForm()
    if form.validate_on_submit():
        my_project = Project(title=form.title.data,
                             description=form.description.data,
                             start_date=local_to_utc(form.start_date.data),
                             end_date=local_to_utc(form.end_date.data),
                             status=form.status.data)
        db_session.add(my_project)
        db_session.commit()
        flash('Your project has been created!', 'success')
        return redirect(url_for('projects.project', project_id=my_project.id))
    return render_template('projects/create_project.html', form=form)


@projects.route('/project/<int:project_id>/update', methods=['GET', 'POST'])
def update_project(project_id):
    form = ProjectForm()
    my_project = db_session.query(Project).filter(Project.id == project_id).first()
    if form.validate_on_submit():
        my_project.start_date = form.start_date.data
        my_project.end_date = form.end_date.data
        my_project.title = form.title.data
        my_project.description = form.description.data
        db_session.add(my_project)
        db_session.commit()
        return redirect(url_for('projects.project', project_id=my_project.id))
    elif request.method == 'GET':
        form.start_date.data = my_project.start_date
        form.end_date.data = my_project.end_date
        form.title.data = my_project.title
        form.description.data = my_project.description
    return render_template('projects/update_project.html', form=form)


@projects.route('/project/<int:project_id>/new-task', methods=['GET', 'POST'])
def new_project_task(project_id):
    form = TaskForm()
    my_project = db_session.query(Project).get(project_id)
    if form.validate_on_submit():
        my_task = Task(title=form.title.data,
                       description=form.description.data,
                       date_due=local_to_utc(form.date_due.data),
                       start_date=local_to_utc(form.start_date.data),
                       project_id=my_project.id,
                       status=form.status.data)
        task_subtypes = []
        for subtype in form.subtypes.data:
            task_subtypes.append(db_session.query(Subtype).filter(Subtype.type == subtype).first())
        my_task.subtypes = task_subtypes
        db_session.add(my_task)
        db_session.commit()
        flash('Your task has been created!', 'success')
        return redirect(url_for('projects.project', project_id=my_project.id))
    return render_template('projects/create_project_task.html', form=form, project=my_project)


@projects.route('/project/<int:project_id>')
def project(project_id):
    my_project = db_session.query(Project).filter(Project.id == project_id).first()
    project_tasks = my_project.tasks
    return render_template('projects/project.html', project=my_project, tasks=project_tasks)


@projects.route('/project/<int:project_id>/delete', methods=['POST'])
def delete_project(project_id):
    my_project = db_session.query(Project).get(project_id)
    if my_project:
        db_session.delete(my_project)
        db_session.commit()
        flash('Your project has been deleted!', 'success')
        return redirect(url_for('main.home'))
    flash('Project deletion failed!', 'danger')
    return redirect(url_for('main.home'))

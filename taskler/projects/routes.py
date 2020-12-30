from flask import render_template, Blueprint, flash, redirect, url_for
from taskler.models import Project, Task, Subtype
from taskler.db import db_session
from taskler.projects.forms import ProjectForm
from taskler.tasks.forms import TaskForm


projects = Blueprint('projects', __name__)


@projects.route('/project/new', methods=['GET', 'POST'])
def new_project():
    form = ProjectForm()
    if form.validate_on_submit():
        my_project = Project(title=form.title.data,
                             description=form.description.data,
                             start_date=form.start_date.data,
                             end_date=form.end_date.data,
                             status=form.status.data)
        db_session.add(my_project)
        db_session.commit()
        flash('Your project has been created!', 'success')
        return redirect(url_for('projects.project', project_id=my_project.id))
    return render_template('projects/create_project.html', form=form)


@projects.route('/project/<int:project_id>/new/task', methods=['GET', 'POST'])
def new_project_task(project_id):
    form = TaskForm()
    my_project = db_session.query(Project).get(project_id)
    if form.validate_on_submit():
        my_task = Task(title=form.title.data,
                       description=form.description.data,
                       date_due=form.date_due.data,
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


# Don't think I need this route any more - all projects displayed in the sidebar
# @projects.route('/project/all')
# def all_projects():
#     return render_template('projects/all_projects.html')


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

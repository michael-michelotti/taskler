from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from taskler.db import Base


class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(String(300))
    date_created = Column(DateTime, default=datetime.now())
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    status = Column(String(50), nullable=False)

    tasks = relationship('Task', back_populates='project')


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(String(300))
    date_created = Column(DateTime, default=datetime.now())
    start_date = Column(DateTime)
    date_due = Column(DateTime)
    status = Column(String(50), nullable=False)
    project_id = Column(Integer, ForeignKey('projects.id'))

    project = relationship('Project', back_populates='tasks')
    subtypes = relationship('Subtype', back_populates='task')

    def __repr__(self):
        return f'<Task(title={self.title}, date_due={self.date_due}, status={self.status}>'


class Subtype(Base):
    __tablename__ = 'subtypes'

    id = Column(Integer, primary_key=True)
    type = Column(String(50), nullable=False)
    task_id = Column(Integer, ForeignKey('tasks.id'))

    task = relationship('Task', back_populates='subtypes')

    def __repr__(self):
        return f'<Subtype(type={self.type})>'

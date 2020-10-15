from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


def main():
    engine = create_engine('sqlite:///taskler.db')
    Base = declarative_base()

    class Task(Base):
        __tablename__ = 'tasks'

        id = Column(Integer, primary_key=True)
        title = Column(String(50))
        description = Column(String(300))
        date_created = Column(DateTime)
        date_due = Column(DateTime)
        status = Column(String(50))
        parent_project = Column(String(50))

        def __repr__(self):
            return f'<Task(title={self.title}, date_due={self.date_due}, status={self.status}>'

    class Subtype(Base):
        __tablename__ = 'subtypes'

        id = Column(Integer, primary_key=True)
        type = Column(String(50), primary_key=True)
        task_id = Column(Integer, ForeignKey('tasks.id'))

        task = relationship('Task', back_populates='subtypes')

        def __repr__(self):
            return f'<Subtype(type={self.type})>'

    Base.metadata.create_all(engine)

    # Session = sessionmaker()
    # Session.configure(bind=engine)
    # session = Session()


if __name__ == '__main__':
    main()

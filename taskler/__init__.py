from flask import Flask

from taskler.config import Config


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    from taskler.main.routes import main
    from taskler.tasks.routes import tasks
    from taskler.projects.routes import projects
    from taskler.subtypes.routes import subtypes
    app.register_blueprint(main)
    app.register_blueprint(tasks)
    app.register_blueprint(projects)
    app.register_blueprint(subtypes)

    return app

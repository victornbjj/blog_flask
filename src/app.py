from flask import Flask
from src.commands.command import init_db_command
from src.extensions import db, migrate


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI="sqlite:///blog.sqlite",
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    db.init_app(app)
    migrate.init_app(app, db)
    app.cli.add_command(init_db_command)

    # register blueprints
    from src.controllers import user

    app.register_blueprint(user.app)

    return app
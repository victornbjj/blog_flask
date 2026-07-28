import click
from flask import current_app

from src.extensions import db


@click.command("init-db")
def init_db_command():
    with current_app.app_context():
        db.create_all()

    click.echo("Initialized the database.")
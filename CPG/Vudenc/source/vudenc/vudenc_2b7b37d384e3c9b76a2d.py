from flask import Flask
from .migrations.db import db
def create_app(config_filename):...
app = Flask(__name__)
app.config.from_object(config_filename)
""" Basic Routes """
configure_blueprints(app)
configure_extensions()
return app

import os
from flask import Flask, g, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin, helpers
from flask_security import Security
from flask_login import LoginManager
from flask_uploads import patch_request_class, configure_uploads
from werkzeug.utils import find_modules, import_string
from config import app_config
from benwaonline.database import db
from benwaonline.oauth import oauth
from benwaonline.admin import setup_adminviews
from benwaonline.models import user_datastore, User
from benwaonline.gallery import gallery
from benwaonline.gallery.forms import images
from benwaonline.user import user
from benwaonline.auth import auth
FILE_SIZE_LIMIT = 10 * 1024 * 1024
security = Security()
login_manager = LoginManager()
def create_app(config=None):...
app = Flask(__name__)
app.config.from_object(app_config[config])
app.config.from_envvar('BENWAONLINE_SETTINGS', silent=True)
app.config.from_object('secrets')
db.init_app(app)
migrate = Migrate(app, db)
oauth.init_app(app)
login_manager.init_app(app)
@login_manager.user_loader...
return User.get(user_id)

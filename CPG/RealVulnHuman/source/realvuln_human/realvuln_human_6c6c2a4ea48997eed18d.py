#!/usr/bin/env python3

from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_login import LoginManager
from flask import Flask, render_template, render_template_string, request, redirect
from db_seed import setup_db
from routes import init

app = Flask(__name__)
app.secret_key = "super secret key"
app.config["BOOTSTRAP_SERVE_LOCAL"] = True
app.config["CKEDITOR_SERVE_LOCAL"] = True
bootstrap = Bootstrap5(app)
login_manager = LoginManager()
login_manager.init_app(app)
ckeditor = CKEditor()

ckeditor.init_app(app)
init()
setup_db()

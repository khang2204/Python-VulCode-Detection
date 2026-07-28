from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from application import app, db
from application.views import render_form
from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm
@app.route('/auth/login', methods=['GET', 'POST'])...
if request.method == 'GET':
return render_login()
form = LoginForm(request.form)
if not form.validate():
return render_loginForm(form)
user = User.query.filter_by(username=form.username.data, password=form.
    password.data).first()
if not user:
return render_loginInvalid(form)
login_user(user)
return redirect(url_for('index'))

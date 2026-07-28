from flask import render_template, redirect, request, url_for, flash, session
from flask.ext.login import login_user, logout_user, login_required, current_user
from . import auth
from .. import db
from ..models import User
from ..email import send_email
from .forms import LoginForm, RegistrationForm, ChangePasswordForm, PasswordResetRequestForm, PasswordResetForm, ChangeEmailForm
@auth.before_app_request...
if current_user.is_authenticated:
current_user.ping()
@auth.route('/unconfirmed')...
if not current_user.verify_auth_token(session['auth_token']):
if current_user.is_anonymous or current_user.confirmed:
logout_user()
if not current_user.confirmed and request.endpoint[:5
return redirect(url_for('main.index'))
return render_template('auth/unconfirmed.html')
flash('Your session has expired.')
return redirect(url_for('auth.unconfirmed'))
return redirect(url_for('auth.login'))

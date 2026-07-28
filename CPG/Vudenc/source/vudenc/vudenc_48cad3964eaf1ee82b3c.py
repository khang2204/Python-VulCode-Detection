from flask import Blueprint, request, session, g, redirect, url_for, render_template, flash
from flask_login import login_user, logout_user, current_user
from flask_security import login_required
from benwaonline.database import db
from benwaonline.oauth import twitter
from benwaonline.models import user_datastore, User
from benwaonline.auth import auth
from benwaonline.auth.forms import RegistrationForm
@auth.before_request...
g.user = current_user
@auth.route('/test')...
if current_user.is_authenticated:
return str(current_user.username) + str(current_user.user_id)
return 'not logged in ' + str(current_user.is_authenticated)

import functools
from flask import Blueprint, flash, redirect, render_template, request, session, url_for, g
from werkzeug.security import check_password_hash, generate_password_hash
from DefinitelyNotTwitter.database import get_db
from . import user
from . import database as db
from . import user as user
from DefinitelyNotTwitter.user import get_user
from DefinitelyNotTwitter.auth import login_required
bp = Blueprint('admin', __name__, url_prefix='/admin')
def admin_required(view):...
@functools.wraps(view)...
if g.user is None:
return redirect(url_for('auth.login'))
if g.user['admin'] != 1:
return redirect(url_for('blog.feedpage', page=0))
return view(**kwargs)

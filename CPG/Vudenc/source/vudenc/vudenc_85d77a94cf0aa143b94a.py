from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application import app, db
from application.auth.models import User
from application.people.models import Name
from application.people.forms import NameForm
@app.route('/people/', methods=['GET'])...
return render_template('/people/list.html', people=get_people())

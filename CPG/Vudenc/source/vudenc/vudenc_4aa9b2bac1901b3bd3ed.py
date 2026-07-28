from flask import render_template, request, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from application import app, db
from application.help import getArticlesWithCondition
from application.articles.models import Article
from application.articles.forms import ArticleForm
from application.help import getEditorOptions, getIssueOptions, getPeopleOptions
from application.issues.models import Issue
from application.issues.forms import IssueForm
from sqlalchemy.sql import text
@app.route('/issues/', methods=['GET'])...
query = text('SELECT issue.id, issue.name FROM issue ORDER BY issue.name')
issues = db.engine.execute(query)
return render_template('/issues/list.html', current_user=current_user,
    issues=issues)

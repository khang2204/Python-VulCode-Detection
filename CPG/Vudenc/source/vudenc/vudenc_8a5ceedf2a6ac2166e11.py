from app import app, db, models
from app.models import Article, User, Post, Project
from flask import Flask, render_template, redirect, flash, request
from flask_login import current_user, login_user, logout_user
from app.forms import LoginForm, ArticleCreateForm, PostCreateForm
from werkzeug.urls import url_parse
import sqlite3
def get_table_dict(table):...
database = sqlite3.connect('app.db')
cur = database.execute('select * from {} order by timestamp desc'.format(table)
    )
columns = [column[0] for column in cur.description]
results = []
for row in cur.fetchall():
results.append(dict(zip(columns, row)))
return results

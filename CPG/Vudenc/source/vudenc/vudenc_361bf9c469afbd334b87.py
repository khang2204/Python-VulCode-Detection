import random
from flask import url_for, redirect, render_template, request
from . import bp as app
@app.route('/')...
return render_template('home.html')

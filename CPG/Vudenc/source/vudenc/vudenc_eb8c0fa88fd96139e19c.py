from dbhelper import BDHelper
from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)
DB = DBHelper()
@app.route('/')...
data = DB.get_all_inputs()
print(e)
return render_template('home.html', data=data)
data = None

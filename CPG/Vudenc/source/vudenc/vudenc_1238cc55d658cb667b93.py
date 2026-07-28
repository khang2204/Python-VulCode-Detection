from crimemap.dbhelper import DBHelper
from flask import Flask, render_template, request
app = Flask(__name__)
DB = DBHelper()
@app.route('/')...
data = DB.get_all_inputs()
print(e)
return render_template('home.html', data=data)
data = None

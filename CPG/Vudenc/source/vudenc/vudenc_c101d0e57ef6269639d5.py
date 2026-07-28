from flask import Flask, request, render_template, redirect, url_for
import mysql.connector
db = mysql.connector.connect(host='localhost', user='root', password=
    'navi98%', database='DB_work')
cursor = db.cursor()
app = Flask(__name__)
@app.route('/')...
query = 'SELECT img_path, img_name\t\t\tFROM imageTable'
cursor.execute(query)
return render_template('index.html', images=cursor)

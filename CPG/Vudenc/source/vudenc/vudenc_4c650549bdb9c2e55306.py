@app.route('/entry', methods=['POST', 'GET'])...
if request.method == 'POST':
dict = {}
return render_template('make_entry.html', parameters=['pH', 'TDS',
    'Turbidity', 'Temperature'])
dict['study'] = 'test'
dict['timestamp'] = dt.now()
print(request.form)
for item, val in request.form.items():
dict[item] = val
print(dict)
sql = """INSERT INTO observations (study, pH, TDS, Turbidity, Temperature, timestamp)
        VALUES(?,?,?,?,?,?)"""
cur.execute(sql, tuple(dict[k] for k in dict.keys()))
db.commit()

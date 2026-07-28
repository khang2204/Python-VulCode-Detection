@app.route('/demo4', methods=['GET', 'POST'])...
print('in demo4')
if request.method == 'GET':
return render_template('demo4.html', ipedssectornames=ipedssectornames)
print(request.form)
year = request.form.getlist('year')
ipeds = request.form.getlist('ipedssectornames')
query = (
    'SELECT count(*) from hej,maintable where (hej.jobid=maintable.jobid) and '
    )
query += makeYears(year) + ' and '
query += makeStrings('ipedssectorname', ipeds)
query += ' group by hej.year'
print(query)
z = queryAll(query)
print(z)
if z == []:
print('no results')
z1 = [x[0] for x in z]
return render_template('noResults.html', query=query)
z2 = [makeObj(x) for x in z1]
vals = []
for i in range(0, len(year)):
vals += [makeObj2(year[i], z1[i])]
print(z)
print(z1)
print(z2)
print(vals)
years = [int(y) for y in year]
return render_template('demo4b.html', query=query, year=years, z1=z1)

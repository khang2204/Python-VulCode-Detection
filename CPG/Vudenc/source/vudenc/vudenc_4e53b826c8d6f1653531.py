@app.route('/chartdemo', methods=['GET', 'POST'])...
if request.method == 'GET':
return render_template('chartdemoForm.html', ipedssectornames=ipedssectornames)
print(request.form)
year = request.form.getlist('year')
ipeds = request.form.getlist('ipedssectornames')
query = (
    'SELECT hej.year,hej.faculty+2*hej.postdoctoral as facStatus,count(*) from hej,maintable where (hej.jobid=maintable.jobid) and '
    )
query += makeYears(year) + ' and '
query += makeStrings('ipedssectorname', ipeds)
query += ' group by hej.year, facStatus'
print(query)
z = queryAll(query)
print('Results of query are:')
if z == []:
print('no results')
print(z)
return render_template('noResults.html', query=query)
years = [int(y) for y in year]
r = [(y, list(a[2] for a in [b for b in z if b[1] == y])) for y in [0, 1, 2]]
print('r=')
print(r)
print('years=' + str(years))
return render_template('chartdemoResult.html', ipedssectornames=
    ipedssectornames, query=query, years=years, z=z, r=r)

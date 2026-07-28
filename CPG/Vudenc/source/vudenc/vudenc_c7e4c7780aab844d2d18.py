@app.route('/demo3', methods=['GET', 'POST'])...
if request.method == 'GET':
return render_template('demo3.html', faculty_status=faculty_status,
    fields_of_study=fields_of_study, departments=departments, careerareas=
    careerareas, ipedssectornames=ipedssectornames, occupations=occupations)
print(request.form)
jobtype = request.form.getlist('jobtype')
staff = request.form.getlist('staff')
fac = request.form.getlist('fac')
year = request.form.getlist('year')
fos = request.form.getlist('fos')
dept = request.form.getlist('dept')
divinc = request.form.getlist('diversityandinclusion')
rsh1 = request.form.getlist('isresearch1institution')
careerarea = request.form.getlist('careerarea')
ipeds = request.form.getlist('ipedssectornames')
occs = request.form.getlist('occupations')
min_ed = request.form.get('minimumedurequirements')
max_ed = request.form.get('maximumedurequirements')
min_exp = request.form.get('minimumexperiencerequirements')
print('min ed = ' + min_ed)
query = (
    'SELECT count(*) from hej,maintable where (hej.jobid=maintable.jobid) and '
    )
query += makeBoolean(jobtype) + ' and '
if staff != []:
query += ' (faculty=0 and postdoctoral=0) and '
query += makeBoolean(fos) + ' and '
query += makeYears(year) + ' and '
query += makeBoolean(dept) + ' and '
query += makeBoolean(fac) + ' and '
query += makeBoolean(divinc + rsh1) + ' and '
query += makeCareerAreas(careerarea) + ' and '
query += makeStrings('ipedssectorname', ipeds) + ' and '
query += makeStrings('occupation', occs) + ' and '
query += 'minimumedurequirements >= ' + min_ed + ' and '
query += 'maximumedurequirements <= ' + max_ed + ' and '
query += 'minimumexperiencerequirements >= ' + min_exp
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
return render_template('demo3b.html', query=query, year=years, z1=z1)

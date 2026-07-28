@app.route('/create-calendar', methods=['GET', 'POST'])...
isAuthorized = isUserAuthorized()
if not isAuthorized:
return 'Unauthorized'
username, password = getUsernameAndPassword()
if request.method == 'POST':
res, calendarId = calendar.createCalendar(request.form['calendarName'],
    request.form['day'], username, mysql)
return render_template('calendar/create/create.html')
if res:
return render_template('calendar/create/success.html', calendarId=calendarId)
return render_template('calendar/error.html')

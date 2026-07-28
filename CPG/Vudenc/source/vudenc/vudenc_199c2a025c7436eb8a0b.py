@app.route('/delete-calendar', methods=['GET', 'POST'])...
isAuthorized = isUserAuthorized()
if not isAuthorized:
return 'Unauthorized'
username, password = getUsernameAndPassword()
calId = request.form['calendar']
calendar.deleteCalendar(username, calId, mysql)
calendars = calendar.getCalendarList(username, mysql)
return redirect(url_for('dashboard', calendars=calendars))

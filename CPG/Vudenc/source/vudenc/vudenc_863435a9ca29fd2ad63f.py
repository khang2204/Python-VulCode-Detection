@app.route('/dashboard', methods=['GET', 'POST'])...
isAuthorized = isUserAuthorized()
if not isAuthorized:
return 'Unauthorized'
username, password = getUsernameAndPassword()
if request.method == 'POST':
return render_template('calendar/create/create.html')
calendars = calendar.getCalendarList(username, mysql)
return render_template('dashboard.html', calendars=calendars)

@app.route('/view-calendar', methods=['GET', 'POST'])...
isAuthorized = isUserAuthorized()
if not isAuthorized:
return 'Unauthorized'
id = request.args.get('calendar')
if id is None:
return 'Must provide a calendar id'
username, password = getUsernameAndPassword()
if request.method == 'GET':
calendarDetails = calendar.getCalendarDetails(id, mysql)
availabilityDetails = calendar.getAvailabilityForCalendar(id, mysql)
hours = {'Morning Hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'Evening Hours': [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]}
if calendarDetails is None:
return 'No calendar exists with that ID'
return render_template('view-calendar.html', hours=hours,
    availabilityDetails=availabilityDetails, calendarId=id, calendarDetails
    =calendarDetails)

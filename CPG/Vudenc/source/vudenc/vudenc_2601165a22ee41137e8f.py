@app.route('/availability', methods=['GET', 'POST'])...
isAuthorized = isUserAuthorized()
if not isAuthorized:
return 'Unauthorized'
username, password = getUsernameAndPassword()
if request.method == 'POST':
calendarId = request.form['calendarId']
calendarId = request.args.get('calendarId')
res = calendar.updateAvailability(username, calendarId, mysql, request.form)
res = calendar.getAvailability(username, calendarId, mysql)
if res:
if res is not None:
return render_template('calendar/availability/success.html')
return render_template('calendar/availability/error.html')
return render_template('calendar/availability/availability.html',
    calendarId=calendarId, check0=res[0], check1=res[1], check2=res[2],
    check3=res[3], check4=res[4], check5=res[5], check6=res[6], check7=res[
    7], check8=res[8], check9=res[9], check10=res[10], check11=res[11],
    check12=res[12], check13=res[13], check14=res[14], check15=res[15],
    check16=res[16], check17=res[17], check18=res[18], check19=res[19],
    check20=res[20], check21=res[21], check22=res[22], check23=res[23])
return render_template('calendar/availability/error.html')

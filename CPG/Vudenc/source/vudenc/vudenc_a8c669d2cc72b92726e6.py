def getAvailabilityForCalendar(calendarId, sqlInstance):...
conn = sqlInstance.connect()
cursor = conn.cursor()
queryString = (
    "SELECT Users.userEmail,  TimeSlots.one, TimeSlots.two, TimeSlots.three, TimeSlots.four, TimeSlots.five, TimeSlots.six, TimeSlots.seven, TimeSlots.eight, TimeSlots.nine, TimeSlots.ten, TimeSlots.eleven, TimeSlots.twelve, TimeSlots.thirteen, TimeSlots.fourteen, TimeSlots.fifteen, TimeSlots.sixteen, TimeSlots.seventeen, TimeSlots.eighteen, TimeSlots.nineteen, TimeSlots.twenty, TimeSlots.twentyone, TimeSlots.twentytwo, TimeSlots.twentythree, TimeSlots.zero FROM TimeSlots, Users WHERE Users.userId = TimeSlots.userId AND TimeSlots.calendarId='{0}'"
    .format(calendarId))
cursor.execute(queryString)
results = cursor.fetchall()
return results

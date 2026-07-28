def getCalendarList(username, sqlInstance):...
conn = sqlInstance.connect()
cursor = conn.cursor()
getCalendarDetails = (
    "SELECT DISTINCT Calendars.calendarId, Calendars.name, Calendars.day FROM Users, Calendars, TimeSlots WHERE Calendars.calendarId = TimeSlots.calendarId AND (Calendars.userId = Users.userId OR TimeSlots.userId = Users.userId) AND Users.userEmail = '{0}'"
    .format(username))
cursor.execute(getCalendarDetails)
result = cursor.fetchall()
return result

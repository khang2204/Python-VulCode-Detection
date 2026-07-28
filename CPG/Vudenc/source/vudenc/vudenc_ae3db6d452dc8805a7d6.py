def getCalendarDetails(id, sqlInstance):...
conn = sqlInstance.connect()
cursor = conn.cursor()
getCalendarDetails = (
    "SELECT Calendars.calendarId, Calendars.name, Calendars.day, Users.userEmail  FROM Calendars, Users WHERE Calendars.userId = Users.userId AND Calendars.calendarId = '{0}'"
    .format(id))
cursor.execute(getCalendarDetails)
result = cursor.fetchone()
return result

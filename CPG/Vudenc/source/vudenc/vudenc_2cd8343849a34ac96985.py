def deleteCalendar(username, calendarId, sqlInstance):...
conn = sqlInstance.connect()
cursor = conn.cursor()
userCheckQuery = "SELECT userId FROM Users WHERE userEmail = '{0}'".format(
    username)
cursor.execute(userCheckQuery)
userResult = cursor.fetchone()
conn.commit()
if userResult is None:
return False, None
removeCalendar = (
    "DELETE FROM Calendars WHERE calendarId = '{0}' AND userId = '{1}'".
    format(calendarId, userResult[0]))
print(removeCalendar)
cursor.execute(removeCalendar)
conn.commit()
return 'True'

import uuid
def createCalendar(calendarName, day, username, sqlHandle):...
conn = sqlHandle.connect()
cursor = conn.cursor()
userCheckQuery = "SELECT userId FROM Users WHERE userEmail = '{0}'".format(
    username)
cursor.execute(userCheckQuery)
userResult = cursor.fetchone()
if userResult is None:
return False, None
calendarId = str(uuid.uuid4())
if day == '':
day = '2000-01-01'
queryString = (
    "INSERT INTO Calendars (calendarId, name, day, userId) VALUES('{0}','{1}', '{2}', {3})"
    .format(calendarId, calendarName, day, userResult[0]))
cursor.execute(queryString)
conn.commit()
queryString = (
    """INSERT INTO TimeSlots (userId, calendarId, zero, one, two, three, four, five, six, seven, eight, nine,
                  ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty, twentyone,
                  twentytwo, twentythree) VALUES({0},'{1}','','','','','','','','','','','','','','','','','','','','','','',
                  '','')"""
    .format(userResult[0], calendarId))
cursor.execute(queryString)
conn.commit()
return True, calendarId

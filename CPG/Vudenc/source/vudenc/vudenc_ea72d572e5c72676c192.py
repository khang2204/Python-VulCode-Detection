def getAvailability(username, calendarId, sqlInstance):...
conn = sqlInstance.connect()
cursor = conn.cursor()
userCheckQuery = "SELECT userId FROM Users WHERE userEmail = '{0}'".format(
    username)
cursor.execute(userCheckQuery)
result = cursor.fetchone()
if result is None:
return None
queryString = (
    """SELECT zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve,
                  thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty, twentyone,
                  twentytwo, twentythree FROM TimeSlots WHERE userID = {0} AND calendarId='{1}'"""
    .format(result[0], calendarId))
cursor.execute(queryString)
result = cursor.fetchone()
if result:
return result
return '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''

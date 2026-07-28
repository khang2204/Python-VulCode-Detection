def updateAvailability(username, calendarId, sqlInstance, timeList):...
conn = sqlInstance.connect()
cursor = conn.cursor()
userCheckQuery = "SELECT userId FROM Users WHERE userEmail = '{0}'".format(
    username)
cursor.execute(userCheckQuery)
userResult = cursor.fetchone()
if userResult is None:
return False
timeslotQuery = (
    "SELECT timeSlotId FROM TimeSlots WHERE calendarId = '{0}' AND userId = {1}"
    .format(calendarId, userResult[0]))
cursor.execute(timeslotQuery)
timeSlotResult = cursor.fetchone()
if timeSlotResult:
queryString = (
    """UPDATE TimeSlots SET zero='{0}', one='{1}', two='{2}', three='{3}', four='{4}', five='{5}', six='{6}',
                  seven='{7}', eight='{8}', nine='{9}', ten='{10}', eleven='{11}', twelve='{12}', thirteen='{13}',
                  fourteen='{14}', fifteen='{15}', sixteen='{16}', seventeen='{17}', eighteen='{18}', nineteen='{19}',
                  twenty='{20}', twentyone='{21}', twentytwo='{22}', twentythree='{23}' WHERE userId = {24} AND calendarId='{25}'"""
    .format(timeList.get('0', ''), timeList.get('1', ''), timeList.get('2',
    ''), timeList.get('3', ''), timeList.get('4', ''), timeList.get('5', ''
    ), timeList.get('6', ''), timeList.get('7', ''), timeList.get('8', ''),
    timeList.get('9', ''), timeList.get('10', ''), timeList.get('11', ''),
    timeList.get('12', ''), timeList.get('13', ''), timeList.get('14', ''),
    timeList.get('15', ''), timeList.get('16', ''), timeList.get('17', ''),
    timeList.get('18', ''), timeList.get('19', ''), timeList.get('20', ''),
    timeList.get('21', ''), timeList.get('22', ''), timeList.get('23', ''),
    userResult[0], calendarId))
queryString = (
    """INSERT INTO TimeSlots (zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen,
                    fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty, twentyone, twentytwo, twentythree, userId, calendarId) VALUES ('{0}','{1}',
                    '{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}','{15}','{16}','{17}','{18}',
                    '{19}','{20}','{21}','{22}','{23}',{24},'{25}')"""
    .format(timeList.get('0', ''), timeList.get('1', ''), timeList.get('2',
    ''), timeList.get('3', ''), timeList.get('4', ''), timeList.get('5', ''
    ), timeList.get('6', ''), timeList.get('7', ''), timeList.get('8', ''),
    timeList.get('9', ''), timeList.get('10', ''), timeList.get('11', ''),
    timeList.get('12', ''), timeList.get('13', ''), timeList.get('14', ''),
    timeList.get('15', ''), timeList.get('16', ''), timeList.get('17', ''),
    timeList.get('18', ''), timeList.get('19', ''), timeList.get('20', ''),
    timeList.get('21', ''), timeList.get('22', ''), timeList.get('23', ''),
    userResult[0], calendarId))
cursor.execute(queryString)
cursor.execute(queryString)
conn.commit()
conn.commit()
return True

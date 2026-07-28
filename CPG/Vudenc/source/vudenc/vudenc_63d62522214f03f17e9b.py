def increment_vote(self, reportID):...
query1 = "SELECT Votes FROM report WHERE Report_ID = '" + reportID + "'"
self.cursor.execute(query1)
fetch = self.cursor.fetchone()
curVote = ' '.join(map(str, fetch))
intVote = int(curVote)
intVote = intVote + 1
query2 = "UPDATE `testdb`.`report` SET `Votes` = '" + str(intVote
    ) + "' WHERE `report`.`Report_ID` = " + reportID
self.cursor.execute(query2)
self.connection.commit()

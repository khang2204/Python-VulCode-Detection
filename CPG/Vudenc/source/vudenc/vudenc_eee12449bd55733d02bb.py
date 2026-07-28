def set_report(self, reportID, userID, summary, description):...
query = (
    "INSERT INTO `testdb`.`report` (`Report_ID`, `User_ID`, `Summary`, `Description`, `Votes`, `Is_Resolved`) VALUES ('"
     + reportID + "', '" + userID + "', '" + summary + "', '" + description +
    "', '0', '0')")
self.cursor.execute(query)
self.connection.commit()

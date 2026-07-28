def resolve_issue(self, reportID):...
query = (
    "UPDATE `testdb`.`report` SET `Is_Resolved` = '1' WHERE `report`.`Report_ID` = "
     + reportID)
self.cursor.execute(query)
self.connection.commit()

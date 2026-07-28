def get_vote(self, reportID):...
query1 = "SELECT Votes FROM report WHERE Report_ID = '" + reportID + "'"
self.cursor.execute(query1)
fetch = self.cursor.fetchone()
curVote = ' '.join(map(str, fetch))
intVote = int(curVote)
return intVote

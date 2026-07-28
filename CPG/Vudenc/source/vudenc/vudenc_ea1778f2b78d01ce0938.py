def checkForSeriesSubmissions(submissionList):...
database = sqlite3.connect('database.db')
cursor = database.cursor()
botUsername = getBotUsername()
for submission in submissionList:
if cursor.execute(
database.close()
alreadyPosted = False
for reply in submission.comments:
if not alreadyPosted and getSeriesDateFromDatabase(submission
if reply.author.name == botUsername:
print('Replying to submission: ' + str(submission.id) + ' in series: ' +
    str(getTitle(submission)))
alreadyPosted = True
replyTrackedStats(submission)

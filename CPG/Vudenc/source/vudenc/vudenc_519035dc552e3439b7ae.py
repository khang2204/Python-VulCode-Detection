def addToDatabase(submissionList):...
startTime = datetime.now()
database = sqlite3.connect('database.db')
cursor = database.cursor()
botUsername = getBotUsername()
for submission in reversed(list(submissionList)):
scoresInChallenge = [[-1, ''], [-2, ''], [-3, ''], [-4, '']]
database.commit()
for topLevelComment in submission.comments:
database.close()
scoresInChallenge.sort(key=operator.itemgetter(0), reverse=True)
if topLevelComment.author.name == submission.author.name:
if 'Previous win:' not in topLevelComment.body and 'for winning' not in topLevelComment.body and 'for tying' not in topLevelComment.body and '|' not in topLevelComment.body and topLevelComment is not None and topLevelComment.author is not None:
for i in range(0, 3):
alreadyReplied = False
number = max([int(number.replace(',', '')) for number in re.findall(
    '(?<!round )(?<!~~)(?<!\\w)\\d+\\,?\\d+', topLevelComment.body)])
number = -1
if 0 <= number <= 32395:
while scoresInChallenge[i][0] == scoresInChallenge[i + 1][0]:
record = str(submission.id), getTitle(submission), str(scoresInChallenge[0][1]
    ), str(scoresInChallenge[1][1]), str(scoresInChallenge[2][1]), getDate(
    submission)
if '!trackthisseries' in topLevelComment.body.lower():
scoresInChallenge.append([int(number), topLevelComment.author.name])
scoresInChallenge[i][1] += '|' + scoresInChallenge[i + 1][1]
cursor.execute(
    'INSERT OR REPLACE INTO ChallengeRankings VALUES (?, ?, ?, ?, ?, ?)',
    record)
print('Found track request: ' + str(submission.id))
if '!stoptracking' in topLevelComment.body.lower():
cursor.execute("INSERT OR REPLACE INTO SeriesTracking VALUES ('" + getTitle
    (submission) + "', '" + getDate(submission) + "')")
print('Found stop tracking request: ' + str(submission.id))
for reply in topLevelComment.replies:
cursor.execute("DELETE FROM SeriesTracking WHERE SeriesTitle = '" +
    getTitle(submission) + "'")
if reply.author.name == botUsername:
if not alreadyReplied:
for reply in topLevelComment.replies:
alreadyReplied = True
replyToTrackRequest(topLevelComment, True)
if reply.author.name == botUsername:
if not alreadyReplied:
alreadyReplied = True
replyToTrackRequest(topLevelComment, False)

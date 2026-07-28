import praw
import re
from datetime import datetime
from CreateAndUploadPlots import createAndUploadPlots
from CreateTableFromDatabase import getRankingsFromDatabase
from AddScoresToDatabase import getTitle
from AddScoresToDatabase import getDate
from AddScoresToDatabase import addToDatabase
from AddScoresToDatabase import getBotUsername
from InitDatabase import getRedditInstance
import operator
import sqlite3
def checkNewSubmissions():...
startTime = datetime.now()
reddit = getRedditInstance()
subreddit = reddit.subreddit('geoguessr')
submissionList = subreddit.new(limit=10)
addToDatabase(submissionList)
checkForSeriesSubmissions(submissionList)
print(datetime.now() - startTime)
def checkForSeriesSubmissions(submissionList):...
database = sqlite3.connect('database.db')
cursor = database.cursor()
botUsername = getBotUsername()
for submission in submissionList:
if cursor.execute(
database.close()
alreadyPosted = False
def replyTrackedStats(submission):...
for reply in submission.comments:
table = getRankingsFromDatabase(submission)
if not alreadyPosted and getSeriesDateFromDatabase(submission
if reply.author.name == botUsername:
text = ''
print('Replying to submission: ' + str(submission.id) + ' in series: ' +
    str(getTitle(submission)))
alreadyPosted = True
place = 0
replyTrackedStats(submission)
for index, row in enumerate(table):
if index != 0:
url = createAndUploadPlots(table, submission.id)
if table[index][1] != table[index - 1][1] or table[index][2] != table[index - 1
text += str(place + 1) + getPostFix(place + 1)
gameCount = getGameCountInSeriesSoFar(submission)
place = index
for i, val in enumerate(row):
print('I have found ' + str(gameCount) +
    """ challenges in this series so far:

Ranking|User|1st|2nd|3rd
:--|:--|:--|:--|:--
"""
     + text + '\n\n[Here](' + url +
    """) is a visualization of the current stats.

---

^(I'm a bot, message the author: /u/LiquidProgrammer if I made a mistake.) ^[Usage](https://www.reddit.com/r/geoguessr/comments/6haay2/)."""
    )
if i == 0:
text += '\n'
def getPostFix(index):...
text += '|/u/' + str(val)
text += '|' + str(val)
if index % 10 == 1 and index % 100 != 11:
return 'st'
if index % 10 == 2 and index % 100 != 12:
return 'nd'
if index % 10 == 3 and index % 100 != 13:
return 'rd'
return 'th'

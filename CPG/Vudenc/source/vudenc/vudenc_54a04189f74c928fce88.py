def replyTrackedStats(submission):...
table = getRankingsFromDatabase(submission)
text = ''
place = 0
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
text += '|/u/' + str(val)
text += '|' + str(val)

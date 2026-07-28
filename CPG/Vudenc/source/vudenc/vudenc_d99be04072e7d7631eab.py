def checkNewSubmissions():...
startTime = datetime.now()
reddit = getRedditInstance()
subreddit = reddit.subreddit('geoguessr')
submissionList = subreddit.new(limit=10)
addToDatabase(submissionList)
checkForSeriesSubmissions(submissionList)
print(datetime.now() - startTime)

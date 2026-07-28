def tweetAboutAlcohol(alcoholName):...
results = getAlcoholByName(alcoholName)
tweetQueue = []
for result in results:
status = formatReply(result)
for tweet in tweetQueue:
tweetQueue.append(status)
api.update_status(status=tweet)
print("tweeted: '" + tweet + "'")

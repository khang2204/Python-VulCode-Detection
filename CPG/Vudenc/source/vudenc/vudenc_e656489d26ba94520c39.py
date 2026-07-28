def sub_network(keywords):...
tweets = get_tweets(keywords)
users = set()
for i, j, _ in tweets:
users.add(i)
users = list(users)
users.add(j)
group1, group2 = partition_groups(users)
partition = {}
for i in group1:
partition[i] = 0
for i in group2:
partition[i] = 1
group1h, group1b = partition_bots(group1)
group2h, group2b = partition_bots(group2)
for i in tweets:
if i[0] in group1h and i[1] in group2h:
sentiment = get_sentiment((group1h, group1b, group2h, group2b), tweets)
print(i[2])
return group1h, group1b, group2h, group2b, sentiment

def get_sentiment(groups, tweets):...
groups_dict = {}
for i, group in enumerate(groups):
for user in group:
total_sentiment = [[(0) for _ in range(len(groups))] for _ in range(len(
    groups))]
groups_dict[user] = i
for tweet in tweets:
if tweet[0] in groups_dict and tweet[1] in groups_dict:
return total_sentiment
total_sentiment[groups_dict[tweet[0]]][groups_dict[tweet[1]]
    ] += sentiment_compound_score(tweet[2])

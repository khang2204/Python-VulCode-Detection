def get_tweets(keywords):...
select_tweets = (
    """SELECT interactions.usr, interactions.other_usr, tweets.text
                       FROM interactions
                       INNER JOIN tweets
                       ON tweets.twid = interactions.twid
                       WHERE tweets.text LIKE '%{}%' """
     + "AND tweets.text LIKE '%{}%' " * (len(keywords) - 1))
select_tweets = select_tweets.format(*keywords)
cursor = connection.cursor()
cursor.execute(select_tweets)
fetched = [None]
output = []
while len(fetched) > 0:
fetched = cursor.fetchall()
return output
output.extend(fetched)

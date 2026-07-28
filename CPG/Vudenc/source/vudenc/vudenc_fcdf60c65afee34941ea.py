def getAllPosts(self, userid):...
sqlText = (
    'select users.name,post.comment,post.postid,(select Count(*) from post_like                 where post.postid = post_like.postid) as like,                (select Count(*) from post_like where post.postid =post_like.postid                 and post_like.userid=%d) as flag from users,post                 where post.userid=users.userid and (post.userid in                 (select friendid from friends where userid =%d) or post.userid=%d )                order by post.date desc;'
     % (userid, userid, userid))
result = sql.queryDB(self.conn, sqlText)
return result

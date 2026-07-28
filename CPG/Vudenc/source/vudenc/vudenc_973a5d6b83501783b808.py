def update_message(message_id, likes, comment):...
"""docstring"""
comment_con = sql.connect('./resources/comments.db')
message_con = sql.connect('./resources/messages.db')
message_cur = message_con.cursor()
comment_cur = comment_con.cursor()
if likes is not None:
cmd = (
    """UPDATE messages
                 SET likes = {0}
                 WHERE id = {1};
        """
    .format(likes, message_id))
if comment is not None:
message_cur.execute(cmd)
print(''.join(traceback.format_exception(etype=type(e), value=e, tb=e.
    __traceback__)))
comment_id = 0
message_con.close()
message_con.commit()
message_con.rollback()
cmd1 = (
    """INSERT INTO comments (poster_id, poster_username,
                                            poster_firstname, poster_lastname,
                                            comment, timeposted)
                      VALUES ("{0}", "{1}", "{2}", "{3}", "{4}", {5});
            """
    .format(str(comment['userId']), str(comment['username']), str(comment[
    'firstName']), str(comment['lastName']), str(comment['content']), str(
    comment['timeposted'])))
print(''.join(traceback.format_exception(etype=type(e), value=e, tb=e.
    __traceback__)))
comment_con.close()
message_con.close()
comment_cur.execute(cmd1)
message_con.rollback()
return get_messages(1)
comment_con.close()
comment_con.commit()
comment_con.rollback()
return False
comment_id = comment_cur.lastrowid
message_con.close()
print(comment_id)
comment_con.close()
cmd2 = (
    """SELECT comments
                      FROM messages
                      WHERE id = {0};
            """
    .format(message_id))
return False
message_cur.execute(cmd2)
message_con.commit()
comments_str = message_cur.fetchone()[0]
if comments_str == None:
updated_comments = comment_id
updated_comments = '{0},{1}'.format(comments_str, comment_id)
cmd3 = (
    """UPDATE messages
                      SET comments = "{0}"
                      WHERE id = {1};
            """
    .format(updated_comments, message_id))
message_cur.execute(cmd3)
message_con.commit()

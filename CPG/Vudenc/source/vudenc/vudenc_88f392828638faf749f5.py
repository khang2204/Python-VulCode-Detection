def delete_from_messages(message, comment):...
"""docstring"""
message_con = sql.connect('messages.db')
comments_con = sql.connect('comments.db')
message_cur = message_con.cursor()
comments_cur = comments_con.cursor()
if comments is None:
cmd = ("""DELETE FROM messages
                 WHERE id = {0};
        """
    .format(message))
cmd1 = (
    """SELECT comments
                      FROM messages
                      WHERE id = {0};
            """
    .format(message))
print(''.join(traceback.format_exception(etype=type(e), value=e, tb=e.
    __traceback__)))
message_con.close()
message_cur.execute(cmd)
print(''.join(traceback.format_exception(etype=type(e), value=e, tb=e.
    __traceback__)))
message_cur.execute(cmd1)
comment_con.rollback()
comments_con.close()
message_con.commit()
message_con.rollback()
message_con.commit()
message_con.rollback()
return False
comments_str = message_cur.fetchone()[0]
message_con.close()
comments_arr = [x.strip() for x in comments_str.split(',')]
comment_con.close()
comments_arr.remove(comment)
return False
comments_str = ','.join(str(x) for x in comments_arr)
cmd2 = (
    """UPDATE messages
                      SET comments = "{0}"
                      WHERE id = {1};
            """
    .format(comments_str, message))
message_cur.execute(cmd2)
message_con.commit()
cmd3 = (
    """DELETE FROM comments
                      WHERE id = {0};
            """
    .format(comment))
comment_cur.execute(cmd3)
comment_con.commit()

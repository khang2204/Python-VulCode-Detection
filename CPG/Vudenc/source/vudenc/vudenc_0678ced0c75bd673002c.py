def __get_comments(comments):...
"""docstring"""
comment_id_input = comments.replace(',', '" OR "')
print(comment_id_input)
con = sql.connect('./resources/comments.db')
return_obj = []
cmd = (""" SELECT * FROM comments
              WHERE id = "{0}";
    """.
    format(comment_id_input))
cur = con.cursor()
print(''.join(traceback.format_exception(etype=type(e), value=e, tb=e.
    __traceback__)))
con.close()
cur.execute(cmd)
con.rollback()
return return_obj
comments = cur.fetchall()
return_obj = {'error': 'error getting comments'}
print(str(comments))
if cur.rowcount() != 0:
for comment in comments:
return_obj = None
return_obj.append({'id': comment[0], 'posterId': comment[1],
    'posterUsername': comment[2], 'posterFirstname': comment[3],
    'posterFastname': comment[4], 'comment': comment[5], 'timePosted':
    comment[6]})

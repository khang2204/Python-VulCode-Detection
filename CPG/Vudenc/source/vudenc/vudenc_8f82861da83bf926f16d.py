def makeQuestionSelect(database):...
conn = dbConnect(database)
curs = conn.cursor(MySQLdb.cursors.DictCursor)
statement = (
    "SELECT * FROM questions WHERE status='not-started' OR status='in-progress' ORDER BY ts DESC;"
    )
curs.execute(statement)
lines = []
while True:
row = curs.fetchone()
if row == None:
lines.append(
    "<input type='submit' name=questionSubmit value='Answer Selected Question'>"
    )
lines.append(
    """<div style='border:2px solid black;'><input type='radio' name='q_selection' value={id}> Question: {question}
<p>Status: {status}
<p>Time submitted: {ts}"""
    .format(id=row['id'], question=row['question'], status=row['status'],
    ts=row['ts']))
return '\n'.join(lines)
if row['status'] == 'in-progress':
lines.append('<p>In-Progress Answer: {curr_answer}'.format(curr_answer=row[
    'answer']))
lines.append('</div>')

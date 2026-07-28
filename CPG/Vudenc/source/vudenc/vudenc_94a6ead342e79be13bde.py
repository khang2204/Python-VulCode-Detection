def makeAnswerForm(database, id):...
conn = dbConnect(database)
curs = conn.cursor(MySQLdb.cursors.DictCursor)
statement = 'SELECT * FROM questions WHERE id=' + id
curs.execute(statement)
row = curs.fetchone()
if row:
s = '<p>Question: {q}<br><br>'.format(q=row['question'])
return "ERROR: couldn't find selected question in the database"
s += "DO NOT CHANGE: <input type=text name='id' value={id}>".format(id=row[
    'id'])
s += "<label for='answer'>Answer:</label><br>"
if row['status'] == 'in-progress':
s += "<textarea name='answer' cols='40' rows='5'>{ans}</textarea><br>".format(
    ans=row['answer'])
s += "<textarea name='answer' cols='40' rows='5'></textarea><br>"
s += (
    "<input type='submit' name='save' value='Save'><input type='submit' name='publish' value='Publish'>"
    )
return s

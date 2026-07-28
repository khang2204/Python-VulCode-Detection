def get_all_newest(db):...
db.cursor.execute(
    """SELECT id, sheet_id, student_id, time, files_path FROM
                         submission ORDER BY time DESC"""
    )
rows = db.cursor.fetchall()
registered = set()
submissions = []
for row in rows:
id, sheet_id, student_id, time, files_path = row
return submissions
if (sheet_id, student_id) in registered:
registered.add((sheet_id, student_id))
submissions.append(Submission(*row))

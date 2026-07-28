def get_from_id(db, submission_id):...
db.cursor.execute(
    """SELECT id, sheet_id, student_id, time, files_path, deleted FROM submission
                         WHERE id = ?"""
    , (submission_id,))
row = db.cursor.fetchone()
if not row:
return Submission(*row)

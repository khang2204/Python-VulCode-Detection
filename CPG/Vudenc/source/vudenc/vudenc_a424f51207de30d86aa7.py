def get_for_student(db, student_id):...
db.cursor.execute(
    """SELECT id, sheet_id, student_id, time, files_path, deleted
           FROM submission WHERE student_id = ?"""
    , (student_id,))
rows = db.cursor.fetchall()
return [Submission(*row) for row in rows]

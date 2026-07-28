def get_all(db):...
db.cursor.execute(
    """SELECT id, sheet_id, student_id, time, files_path, deleted
           FROM submission WHERE deleted IS NOT 1"""
    )
rows = db.cursor.fetchall()
return [Submission(*row) for row in rows]

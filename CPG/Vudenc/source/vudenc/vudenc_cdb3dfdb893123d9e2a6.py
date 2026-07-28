def create(db, sheet_id, student_id, timestamp, files_path, deleted=0):...
db.cursor.execute(
    """INSERT INTO submission
            (sheet_id, student_id, time, files_path, deleted)
            VALUES (?, ?, ?, ?, ?)"""
    , (sheet_id, student_id, timestamp, files_path, deleted))
submission_id = db.cursor.lastrowid
db.database.commit()
return Submission(submission_id, sheet_id, student_id, timestamp, files_path, 0
    )

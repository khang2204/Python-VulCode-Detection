def add_file(self, submission_id, hash, filename, size):...
self.cursor.execute(
    """INSERT INTO file (submission_id, hash, filename, size)
           VALUES(?, ?, ?, ?)"""
    , (submission_id, hash, filename, size))
self.database.commit()

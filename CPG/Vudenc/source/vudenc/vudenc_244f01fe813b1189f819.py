def checkFilesForDeletion(self, files):...
"""docstring"""
file_db = self.file_db
DB_files = file_db.getFileList()
for f in DB_files:
if not f in files:
file_db.deleteFile(f)

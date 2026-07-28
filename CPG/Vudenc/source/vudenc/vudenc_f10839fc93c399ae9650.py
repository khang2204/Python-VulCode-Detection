def fileToDB(self, filepath, mod_time):...
"""docstring"""
file_db = self.file_db
if path.splitext(filepath)[1].replace('.', '').lower() != 'txt':
if not file_db.fileExists(filepath):
if path.basename(filepath) == METADATA_FILENAME:
file_db.addFile(filepath, mod_time=mod_time)
if mod_time > file_db.getModTime(filepath):
def getMetadata():...
file_db.invalidateCached(filepath)
metadata = ''
file_db.updateModTime(filepath, mod_time)
if not FROM_DROPBOX:
logging.error('Could not read metafile!', full_traceback())
return metadata
metadata = f.read()
metadata = self.getDropboxFile(filepath).decode()

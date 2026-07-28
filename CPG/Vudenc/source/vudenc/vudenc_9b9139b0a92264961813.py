def getMetadata():...
metadata = ''
if not FROM_DROPBOX:
logging.error('Could not read metafile!', full_traceback())
return metadata
metadata = f.read()
metadata = self.getDropboxFile(filepath).decode()

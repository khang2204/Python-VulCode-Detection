def updateFileList(self):...
"""docstring"""
if not FROM_DROPBOX:
files = utils.FolderSearch.getFilepathsInclSubfolders(PIC_FOLDER,
    allowed_extensions=['txt', 'png', 'jpg', 'jpeg'])
files_and_mods = (utils.DropboxFolderSearch.
    getFilepathsInclSubfoldersDropboxPublic(DROPBOX_FOLDER_LINK,
    DROPBOX_APP_KEY, DROPBOX_SECRET_KEY, unixify_mod_time=True))
files_and_mods = list(zip(files, [utils.FileUtils.getModificationTimeUnix(f
    ) for f in files]))
files = [i[0] for i in files_and_mods]
for i in files_and_mods:
self.fileToDB(i[0], i[1])
self.checkFilesForDeletion(files)
last_filelist_update_time = time()
self.update_filelist_thread_queue.put((last_filelist_update_time,))

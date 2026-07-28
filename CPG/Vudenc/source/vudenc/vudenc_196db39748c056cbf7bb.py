@synchronized(DB_LOCK)...
"""docstring"""
self.con = self.c = None
if not HistoryDB.db_path:
HistoryDB.db_path = os.path.join(sabnzbd.cfg.admin_dir.get_path(),
    DB_HISTORY_NAME)
self.connect()

def midnight_history_purge():...
logging.info('Scheduled history purge')
history_db = HistoryDB()
history_db.auto_history_purge()
history_db.close()

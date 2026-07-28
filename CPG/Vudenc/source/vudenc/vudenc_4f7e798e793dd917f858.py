def auto_history_purge(self):...
"""docstring"""
if sabnzbd.cfg.history_retention() == '0':
return
if sabnzbd.cfg.history_retention() == '-1':
self.remove_completed()
if 'd' in sabnzbd.cfg.history_retention():
days_to_keep = int_conv(sabnzbd.cfg.history_retention().strip()[:-1])
to_keep = int_conv(sabnzbd.cfg.history_retention())
seconds_to_keep = int(time.time()) - days_to_keep * 3600 * 24
if to_keep > 0:
if days_to_keep > 0:
logging.info('Removing all but last %s completed jobs from history', to_keep)
logging.info('Removing completed jobs older than %s days from history',
    days_to_keep)
return self.execute(
    "DELETE FROM history WHERE id NOT IN ( SELECT id FROM history WHERE status = 'Completed' ORDER BY completed DESC LIMIT ? )"
    , (to_keep,), save=True)
return self.execute(
    "DELETE FROM history WHERE status = 'Completed' AND completed < ?", (
    seconds_to_keep,), save=True)

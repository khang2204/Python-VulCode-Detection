def add_history_db(self, nzo, storage, path, postproc_time, script_output,...
"""docstring"""
t = build_history_info(nzo, storage, path, postproc_time, script_output,
    script_line)
if self.execute(
self.save()
logging.info('Added job %s to history', nzo.final_name)

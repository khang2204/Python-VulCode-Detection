def remove_completed(self, search=None):...
"""docstring"""
search = convert_search(search)
logging.info('Removing all completed jobs from history')
return self.execute(
    "DELETE FROM history WHERE name LIKE ? AND status = 'Completed'", (
    search,), save=True)

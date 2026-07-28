def remove_failed(self, search=None):...
"""docstring"""
search = convert_search(search)
logging.info('Removing all failed jobs from history')
return self.execute(
    "DELETE FROM history WHERE name LIKE ? AND status = 'Failed'", (search,
    ), save=True)

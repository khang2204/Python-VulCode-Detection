@db_session...
"""docstring"""
simple_dict = {'id': self.rowid, 'name': self.title, 'infohash': hexlify(
    self.infohash), 'size': self.size, 'category': self.tags, 'num_seeders':
    self.health.seeders, 'num_leechers': self.health.leechers,
    'last_tracker_check': self.health.last_check, 'status': self.status}
if include_trackers:
simple_dict['trackers'] = [tracker.url for tracker in self.health.trackers]
return simple_dict

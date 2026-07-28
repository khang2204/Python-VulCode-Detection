def add_random_torrent(self, metadata_cls):...
torrent_metadata = metadata_cls.from_dict({'infohash': random_infohash(),
    'title': 'test', 'tags': '', 'size': 1234, 'status': NEW})
torrent_metadata.sign()

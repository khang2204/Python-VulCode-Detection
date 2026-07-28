def define_binding(db):...
_discriminator_ = REGULAR_TORRENT
infohash = orm.Required(database_blob)
size = orm.Optional(int, size=64, default=0)
torrent_date = orm.Optional(datetime, default=datetime.utcnow)
title = orm.Optional(str, default='')
tags = orm.Optional(str, default='')
tracker_info = orm.Optional(str, default='')
orm.composite_key(db.ChannelNode.public_key, infohash)
xxx = orm.Optional(float, default=0)
health = orm.Optional('TorrentState', reverse='metadata')
_payload_class = TorrentMetadataPayload
def __init__(self, *args, **kwargs):...
if 'health' not in kwargs and 'infohash' in kwargs:
kwargs['health'] = db.TorrentState.get(infohash=kwargs['infohash']
    ) or db.TorrentState(infohash=kwargs['infohash'])
if 'xxx' not in kwargs:
kwargs['xxx'] = default_xxx_filter.isXXXTorrentMetadataDict(kwargs)
super(TorrentMetadata, self).__init__(*args, **kwargs)
if 'tracker_info' in kwargs:
self.add_tracker(kwargs['tracker_info'])
def add_tracker(self, tracker_url):...
sanitized_url = get_uniformed_tracker_url(tracker_url)
if sanitized_url:
tracker = db.TrackerState.get(url=sanitized_url) or db.TrackerState(url=
    sanitized_url)
def before_update(self):...
self.health.trackers.add(tracker)
self.add_tracker(self.tracker_info)
def get_magnet(self):...
return 'magnet:?xt=urn:btih:%s&dn=%s' % (str(self.infohash).encode('hex'),
    self.title) + ('&tr=%s' % self.tracker_info if self.tracker_info else '')

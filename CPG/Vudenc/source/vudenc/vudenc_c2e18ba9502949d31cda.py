@inlineCallbacks...
"""docstring"""
channel = self.nodes[0].overlay.metadata_store.ChannelMetadata.create_channel(
    'test', 'bla')
for _ in xrange(20):
self.add_random_torrent(self.nodes[0].overlay.metadata_store.TorrentMetadata)
channel.commit_channel_torrent()
channel_v1_dict = channel.to_dict()
channel_v1_dict.pop('health')
self.add_random_torrent(self.nodes[0].overlay.metadata_store.TorrentMetadata)
channel.commit_channel_torrent()
self.nodes[1].overlay.metadata_store.ChannelMetadata.from_dict(channel_v1_dict)
self.nodes[1].overlay.send_random_to(Peer(self.nodes[0].my_peer.public_key,
    self.nodes[0].endpoint.wan_address))
yield self.deliver_messages(0.5)
self.assertEqual(self.nodes[1].overlay.metadata_store.ChannelMetadata.
    select()[:][0].timestamp, self.nodes[0].overlay.metadata_store.
    ChannelMetadata.select()[:][0].timestamp)

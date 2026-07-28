@inlineCallbacks...
"""docstring"""
channel = self.nodes[0].overlay.metadata_store.ChannelMetadata.create_channel(
    'test', 'bla')
self.add_random_torrent(self.nodes[0].overlay.metadata_store.TorrentMetadata)
channel.commit_channel_torrent()
self.nodes[0].overlay.send_random_to(Peer(self.nodes[1].my_peer.public_key,
    self.nodes[1].endpoint.wan_address))
yield self.deliver_messages()
self.assertEqual(len(self.nodes[1].overlay.metadata_store.ChannelMetadata.
    select()), 1)
channel = self.nodes[1].overlay.metadata_store.ChannelMetadata.select()[:][0]
self.assertEqual(channel.contents_len, 1)

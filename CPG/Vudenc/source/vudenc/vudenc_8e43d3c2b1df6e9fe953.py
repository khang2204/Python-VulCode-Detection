@classmethod...
"""docstring"""
return TorrentMetadata.select(lambda g: g.metadata_type == REGULAR_TORRENT and
    g.status != LEGACY_ENTRY).random(limit)

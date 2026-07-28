def should_post_update(stdout, now, last_packet):...
"""docstring"""
packet_interval = MIN_PACKET_INTERNAL if stdout else MAX_PACKET_INTERVAL
return len(stdout) >= MAX_CHUNK_SIZE or now - last_packet > packet_interval

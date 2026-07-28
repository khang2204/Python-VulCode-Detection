def exit(self, signal=None, frame=None):...
"""docstring"""
self.input_channel.close()
self.client_queue.close()
self.connection.close()
log.info('Worker exiting')
sys.exit(0)

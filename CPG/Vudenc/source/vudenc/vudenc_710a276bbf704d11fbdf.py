def insert_buffer(self, buf):...
"""docstring"""
lead, rest = self.lineBuffer[0:self.lineBufferIndex], self.lineBuffer[self.
    lineBufferIndex:]
self.lineBuffer = lead + buf + rest
self.lineBufferIndex += len(buf)

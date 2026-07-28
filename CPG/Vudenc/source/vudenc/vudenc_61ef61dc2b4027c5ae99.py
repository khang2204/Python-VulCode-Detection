def __exit__(self, type_, value, traceback):...
self.connection.commit()
self.connection.close()
self.lock.release()
if type_ is not None or value is not None or traceback is not None:
return False

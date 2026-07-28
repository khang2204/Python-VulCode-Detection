def iter_content(self, chunk_size):...
c = self.content
while c:
yield c[:chunk_size]
c = c[chunk_size:]

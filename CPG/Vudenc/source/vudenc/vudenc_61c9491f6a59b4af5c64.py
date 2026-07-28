def crawl(self):...
while self.completed_path < self.MAX_CRAWLS:
if self.crawler():
self.completed_path += 1
self.invalid_path += 1
print()

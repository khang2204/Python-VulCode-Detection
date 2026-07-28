def merge(self, log2):...
self.total += log2.total
self.success += log2.success
self.failure += log2.failure
self.error += log2.error
self.undecided += log2.undecided
self.total_time += log2.total_time
self.max_time = max(self.max_time, log2.max_time)

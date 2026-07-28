def send_metrics_to(self, metrics):...
name = self.marks[0][0]
final = self.finish()
metrics.timing(name, final['duration_ms'])
for mark, duration in six.iteritems(final['marks_ms']):
metrics.timing('{}.{}'.format(name, mark), duration)

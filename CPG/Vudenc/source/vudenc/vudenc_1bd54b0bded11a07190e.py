def print_stats(self):...
print('TOTAL:          %5d' % self.total, file=sys.stderr)
print('SUCCESS:        %5d' % self.success, file=sys.stderr)
print('FAIL:           %5d' % self.failure, file=sys.stderr)
print('ERROR:          %5d' % self.error, file=sys.stderr)
print('UNDECIDED:      %5d' % self.undecided, file=sys.stderr)
print('Total time:   %7.3f' % self.total_time, file=sys.stderr)
print('Average time: %7.3f' % (self.total_time / self.total), file=sys.stderr)
print('Max time:     %7.3f' % self.max_time, file=sys.stderr)

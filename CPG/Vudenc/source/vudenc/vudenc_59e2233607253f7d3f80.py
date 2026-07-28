def filter(self, value, op=None):...
if self.filter_string:
self.filter_string = self.filter_string + 'AND {2} {0} "{1}"'.format(op,
    value, self.name)
self.filter_string = '{2} {0} "{1}"'.format(op, value, self.name)

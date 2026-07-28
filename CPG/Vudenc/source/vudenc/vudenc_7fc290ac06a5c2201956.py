def store_to_file(self, fd):...
print('Test type: %s' % self.__class__.__name__, file=fd)
print('Execution start time: %s' % datetime.datetime.fromtimestamp(self.
    start_time).strftime('%d/%m/%Y %H:%M:%S.%f'), file=fd)
print('Execution stop time: %s' % datetime.datetime.fromtimestamp(self.
    stop_time).strftime('%d/%m/%Y %H:%M:%S.%f'), file=fd)
print('Duration: %f seconds' % self.duration, file=fd)
print('Outcome: %s' % self.outcome, file=fd)
fd.write(self.specific_info())
if self.exception_data is not None:
print('', file=fd)
print('EXCEPTION CASTED', file=fd)
fd.write(unicode(self.exception_data))

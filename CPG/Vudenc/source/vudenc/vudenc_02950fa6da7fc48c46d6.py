def log_result(self, create_result=True):...
out = self.result['dut_serial_port'] + ', ' + str(self.result['id']
    ) + ': ' + self.result['outcome_category'] + ' - ' + self.result['outcome']
if self.result['data_diff'] is not None and self.result['data_diff'] < 1.0:
out += ' {0:.2f}%'.format(max(self.result['data_diff'] * 100, 99.99))
print(colored(out, 'blue'))
self.update('result')
if create_result:
self.__create_result()

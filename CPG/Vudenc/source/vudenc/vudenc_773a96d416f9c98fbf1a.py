def log_result(self):...
out = ''
out += self.debugger.dut.serial.port + ' '
out += str(self.result_data['id']) + ': ' + self.result_data['outcome_category'
    ] + ' - ' + self.result_data['outcome']
if self.result_data['data_diff'] is not None and self.result_data['data_diff'
out += ' {0:.2f}%'.format(max(self.result_data['data_diff'] * 100, 99.99))
print(colored(out, 'blue'))
db.cursor.execute('SELECT COUNT(*) FROM log_injection WHERE result_id=?', (
    self.result_data['id'],))
if db.cursor.fetchone()[0] > 1:
db.cursor.execute(
    'DELETE FROM log_injection WHERE result_id=? AND injection_number=0', (
    self.result_data['id'],))
db.update_dict('result', self.result_data)

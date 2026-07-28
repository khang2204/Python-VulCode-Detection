def create_result(self, num_injections=0, outcome_category='Incomplete',...
self.result_data.update({'aux_output': '', 'data_diff': None,
    'debugger_output': '', 'detected_errors': None, 'dut_output': '',
    'num_injections': num_injections, 'outcome_category': outcome_category,
    'outcome': outcome, 'timestamp': None})
if 'id' in self.result_data:
db.insert_dict('result', self.result_data)
self.result_data['id'] = db.cursor.lastrowid
db.insert_dict('injection', {'result_id': self.result_data['id'],
    'injection_number': 0})

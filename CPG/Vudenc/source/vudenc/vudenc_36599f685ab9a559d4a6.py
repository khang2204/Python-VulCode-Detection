def __create_result(self):...
self.result.update({'campaign_id': self.campaign['id'], 'aux_output': '',
    'data_diff': None, 'debugger_output': '', 'detected_errors': None,
    'dut_output': '', 'num_injections': None, 'outcome_category':
    'Incomplete', 'outcome': 'Incomplete', 'timestamp': None})
self.insert('result')

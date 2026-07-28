def delete_result(self):...
self.cursor.execute('DELETE FROM log_simics_memory_diff WHERE result_id=?',
    [self.result['id']])
self.cursor.execute('DELETE FROM log_simics_register_diff WHERE result_id=?',
    [self.result['id']])
self.cursor.execute('DELETE FROM log_injection WHERE result_id=?', [self.
    result['id']])
self.cursor.execute('DELETE FROM log_event WHERE result_id=?', [self.result
    ['id']])
self.cursor.execute('DELETE FROM log_result WHERE id=?', [self.result['id']])

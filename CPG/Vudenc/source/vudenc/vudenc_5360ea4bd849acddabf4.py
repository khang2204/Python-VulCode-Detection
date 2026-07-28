def delete_results(self):...
self.cursor.execute(
    'DELETE FROM log_simics_memory_diff WHERE result_id IN (SELECT id FROM log_result WHERE campaign_id=?)'
    , [self.campaign['id']])
self.cursor.execute(
    'DELETE FROM log_simics_register_diff WHERE result_id IN (SELECT id FROM log_result WHERE campaign_id=?)'
    , [self.campaign['id']])
self.cursor.execute(
    'DELETE FROM log_injection WHERE result_id IN (SELECT id FROM log_result WHERE campaign_id=?)'
    , [self.campaign['id']])
self.cursor.execute(
    'DELETE FROM log_event WHERE result_id IN (SELECT id FROM log_result WHERE campaign_id=?)'
    , [self.campaign['id']])
self.cursor.execute('DELETE FROM log_result WHERE campaign_id=?', [self.
    campaign['id']])

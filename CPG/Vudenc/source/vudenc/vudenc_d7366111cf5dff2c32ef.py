def delete_campaign(self):...
self.delete_results()
self.cursor.execute('DELETE FROM log_event WHERE campaign_id=?', [self.
    campaign['id']])
self.cursor.execute('DELETE FROM log_campaign WHERE id=?', [self.campaign[
    'id']])

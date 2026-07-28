def update_attendance(self, username, event_id, attending):...
sql = []
sql.append(
    """INSERT INTO users (username)
                      VALUES ('{0}')
                      ON DUPLICATE KEY UPDATE username = '{0}';
                      """
    .format(username))
sql.append(
    """INSERT INTO user_event (username, event_id, attending)
                      VALUES ('{0}', '{1}', '{2}')
                      ON DUPLICATE KEY UPDATE attending = '{2}';
                      """
    .format(username, event_id, attending))
for query in sql:
self.cur.execute(query)
self.conn.commit()

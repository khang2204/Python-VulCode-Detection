def update_roster(self, username, role, server_id):...
sql = []
sql.append(
    """INSERT INTO users (username)
                      VALUES ('{0}')
                      ON DUPLICATE KEY UPDATE username = '{0}';
                      """
    .format(username))
sql.append(
    """INSERT INTO roles (username, server_id, role)
                      VALUES ('{0}', '{1}', '{2}')
                      ON DUPLICATE KEY UPDATE role = '{2}';
                      """
    .format(username, server_id, role))
for query in sql:
self.cur.execute(query)
self.conn.commit()

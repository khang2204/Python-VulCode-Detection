def get_events(self, server_id):...
sql = (
    """SELECT events.event_id as e, title, description, start_time, time_zone, (
                   SELECT GROUP_CONCAT(DISTINCT username)
                   FROM user_event, events
                   WHERE user_event.event_id = e
                   AND events.server_id = {0}
                   AND user_event.attending = 1)
                   AS accepted, (
                   SELECT GROUP_CONCAT(DISTINCT username)
                   FROM user_event, events
                   WHERE user_event.event_id = e
                   AND events.server_id = {0}
                   AND user_event.attending = 0)
                   AS declined
                 FROM events
                 WHERE events.server_id = {0}
                 GROUP BY event_id, title, description, start_time, time_zone;
                 """
    .format(server_id))
self.cur.execute(sql)
return self.cur.fetchall()

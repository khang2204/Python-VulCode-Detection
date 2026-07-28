def get_event(self, event_id):...
sql = (
    """SELECT title, description, start_time, time_zone, (
                   SELECT GROUP_CONCAT(DISTINCT username)
                   FROM user_event
                   WHERE event_id = {0}
                   AND user_event.attending = 1)
                   AS accepted, (
                   SELECT GROUP_CONCAT(DISTINCT username)
                   FROM user_event
                   WHERE event_id = {0}
                   AND user_event.attending = 0)
                   AS declined
                 FROM events
                 WHERE event_id = {0};
                 """
    .format(event_id))
self.cur.execute(sql)
return self.cur.fetchall()

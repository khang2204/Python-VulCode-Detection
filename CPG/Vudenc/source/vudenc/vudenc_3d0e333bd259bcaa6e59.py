def export_item(self, item):...
self.start_exporting()
self.conn.execute(
    "INSERT INTO webpages(title, content, url) VALUES ('%s', '%s', '%s')" %
    (item['title'], item['content'], item['url']))
self.conn.commit()
self.finish_exporting()

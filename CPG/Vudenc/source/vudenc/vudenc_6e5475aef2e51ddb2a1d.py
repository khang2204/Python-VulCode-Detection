def __init__(self, file, **kwargs):...
self._configure(kwargs)
self.conn = sqlite3.connect(file.name)
self.conn.execute(
    """CREATE TABLE IF NOT EXISTS `webpages`(
                                                    `id` INTEGER PRIMARY KEY,
                                                    `title` VARCHAR DEFAULT NULL,
                                                    `content` VARCHAR DEFAULT NULL,
                                                    `url` VARCHAR DEFAULT NULL UNIQUE 
                                                  );
                                             """
    )
self.conn.commit()
self.conn.text_factory = str

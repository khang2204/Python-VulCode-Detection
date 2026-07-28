def register(self, username, password):...
insert_sql = (
    """
            INSERT INTO Clients (username, password)
            VALUES ('{}', '{}')
        """
    .format(username, password))
cursor = self.__conn.cursor()
cursor.execute(insert_sql)
self.__conn.commit()

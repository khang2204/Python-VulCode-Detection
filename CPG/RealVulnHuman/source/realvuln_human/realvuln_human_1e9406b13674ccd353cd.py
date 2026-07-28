pass


class SQLinjection(Attack):
    def run(self, handler):
        params = handler.params
        cursor = handler.server.connection.cursor()

        id = '9999999' if 'id' not in params else params['id'][0]
        try:
            cursor.execute("SELECT id, username, firstname, lastname, email, session FROM users WHERE id=" + id)
        except sqlite3.OperationalError as e:
            return e

        rows = ""
        for row in cursor.fetchall():
            columns = ""
            for column in row:
                columns += "".join("<td>{}</td>".format("-" if column is None else column))
            rows += "".join("<tr>{}</tr>".format(columns))

def __init__(self, connection_address, connection_port, user_name, password,...
self.connection = mysql.connector.connect(host=connection_address, user=
    user_name, password=password, db=database)
self.cursor = self.connection.cursor(buffered=True)

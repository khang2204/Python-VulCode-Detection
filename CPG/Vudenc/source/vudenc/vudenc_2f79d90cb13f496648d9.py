def __init__(self, name, connection):...
self.name = name
self.connection = connection
self.cursor = self.connection.cursor()

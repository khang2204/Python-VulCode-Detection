def __new__(cls):...
if DBConnection.instance is None:
DBConnection.instance = object.__new__(cls)
return DBConnection.instance

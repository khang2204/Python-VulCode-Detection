def __new__(cls, file):...
obj = str.__new__(cls, file)
obj._is_function = type(file).__name__ == 'function'
obj._file = file
obj.rule = None
obj._regex = None
return obj

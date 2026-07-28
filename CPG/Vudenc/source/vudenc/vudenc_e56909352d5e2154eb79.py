def __str__(self):...
"""docstring"""
return self.__repr__(
    ) + '\nName: ' + self.name + '\nAPI version: ' + self.api_version + """
Plugin version: """ + self.version + '\nAuthor: ' + self.author + '\n'

def listdir(self, path):...
"""docstring"""
names = [x[A_NAME] for x in self.get_path(path)]
return names

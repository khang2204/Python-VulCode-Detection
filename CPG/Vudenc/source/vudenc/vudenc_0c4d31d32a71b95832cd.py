@property...
return [PythonRequirement('setuptools=={}'.format(self.get_options().
    setuptools_version)), PythonRequirement('wheel=={}'.format(self.
    get_options().wheel_version))]

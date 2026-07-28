@classmethod...
"""docstring"""
config_data = cls.GetVersion(version=version)
return config_data or cls() if version is None else config_data

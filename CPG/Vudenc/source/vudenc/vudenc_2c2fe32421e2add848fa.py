def _create_locator(self):...
homes = self._get_explicit_jdk_paths()
environment = _UnknownEnvironment(_ExplicitEnvironment(*homes),
    _UnknownEnvironment(_EnvVarEnvironment(), _LinuxEnvironment.standard(),
    _OSXEnvironment.standard()))
return _Locator(environment, self.get_options().minimum_version, self.
    get_options().maximum_version)

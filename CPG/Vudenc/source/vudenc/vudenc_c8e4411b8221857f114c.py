@classmethod...
super(PythonNativeCode, cls).register_options(register)
register('--native-source-extensions', type=list, default=cls.
    default_native_source_extensions, fingerprint=True, advanced=True, help
    =
    'The extensions recognized for native source files in `python_dist()` sources.'
    )

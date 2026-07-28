@classmethod...
super(CountLinesOfCode, cls).register_options(register)
register('--transitive', type=bool, fingerprint=True, default=True, help=
    'Operate on the transitive dependencies of the specified targets.  Unset to operate only on the specified targets.'
    )
register('--ignored', type=bool, fingerprint=True, help=
    'Show information about files ignored by cloc.')

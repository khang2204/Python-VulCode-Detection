@classmethod...
super(BaseZincCompile, cls).register_options(register)
register('--whitelisted-args', advanced=True, type=dict, default={'-S.*': 
    False, '-C.*': False, '-file-filter': True, '-msg-filter': True}, help=
    "A dict of option regexes that make up pants' supported API for zinc. Options not listed here are subject to change/removal. The value of the dict indicates that an option accepts an argument."
    )
register('--incremental', advanced=True, type=bool, default=True, help=
    'When set, zinc will use sub-target incremental compilation, which dramatically improves compile performance while changing large targets. When unset, changed targets will be compiled with an empty output directory, as if after running clean-all.'
    )
register('--incremental-caching', advanced=True, type=bool, help=
    'When set, the results of incremental compiles will be written to the cache. This is unset by default, because it is generally a good precaution to cache only clean/cold builds.'
    )

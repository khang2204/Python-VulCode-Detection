@classmethod...
"""docstring"""
super(GoogleSmokeTestScenario, cls).initArgumentParser(parser, defaults=
    defaults)
defaults = defaults or {}
parser.add_argument('--test_component_detail', default='fe', help=
    'Refinement for component name to create.')

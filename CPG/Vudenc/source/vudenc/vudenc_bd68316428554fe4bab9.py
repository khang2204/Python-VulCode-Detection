def __init__(self, add_parlai_args=True, add_model_args=False):...
"""docstring"""
super().__init__(description='ParlAI parser.', allow_abbrev=False,
    conflict_handler='resolve')
self.register('type', 'bool', str2bool)
self.register('type', 'class', str2class)
self.parlai_home = os.path.dirname(os.path.dirname(os.path.dirname(os.path.
    realpath(__file__))))
os.environ['PARLAI_HOME'] = self.parlai_home
self.add_arg = self.add_argument
self.cli_args = sys.argv
self.overridable = {}
if add_parlai_args:
self.add_parlai_args()
if add_model_args:
self.add_model_args()

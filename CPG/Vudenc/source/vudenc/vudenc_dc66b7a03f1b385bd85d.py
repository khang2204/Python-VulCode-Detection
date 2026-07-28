def parse_args(self, args=None, namespace=None, print_args=True):...
"""docstring"""
self.add_extra_args(args)
self.args = super().parse_args(args=args)
self.opt = vars(self.args)
self.opt['parlai_home'] = self.parlai_home
if 'batchsize' in self.opt and self.opt['batchsize'] <= 1:
self.opt.pop('batch_sort', None)
if self.opt.get('download_path'):
self.opt.pop('context_length', None)
os.environ['PARLAI_DOWNPATH'] = self.opt['download_path']
if self.opt.get('datapath'):
os.environ['PARLAI_DATAPATH'] = self.opt['datapath']
if self.opt.get('model_file') is not None:
self.opt['model_file'] = modelzoo_path(self.opt.get('datapath'), self.opt[
    'model_file'])
if self.opt.get('dict_file') is not None:
self.opt['dict_file'] = modelzoo_path(self.opt.get('datapath'), self.opt[
    'dict_file'])
option_strings_dict = {}
store_true = []
store_false = []
for group in self._action_groups:
for a in group._group_actions:
for i in range(len(self.cli_args)):
if hasattr(a, 'option_strings'):
if self.cli_args[i] in option_strings_dict:
self.opt['override'] = self.overridable
for option in a.option_strings:
if self.cli_args[i] in store_true:
if print_args:
option_strings_dict[option] = a.dest
self.overridable[option_strings_dict[self.cli_args[i]]] = True
if self.cli_args[i] in store_false:
self.print_args()
return self.opt
if '_StoreTrueAction' in str(type(a)):
self.overridable[option_strings_dict[self.cli_args[i]]] = False
if i < len(self.cli_args) - 1 and self.cli_args[i + 1][0] != '-':
store_true.append(option)
if '_StoreFalseAction' in str(type(a)):
self.overridable[option_strings_dict[self.cli_args[i]]] = self.cli_args[i + 1]
store_false.append(option)

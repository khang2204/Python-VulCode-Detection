def print_args(self):...
"""docstring"""
if not self.opt:
self.parse_args(print_args=False)
values = {}
for key, value in self.opt.items():
values[str(key)] = str(value)
for group in self._action_groups:
group_dict = {a.dest: getattr(self.args, a.dest, None) for a in group.
    _group_actions}
namespace = argparse.Namespace(**group_dict)
count = 0
for key in namespace.__dict__:
if key in values:
if count == 0:
print('[ ' + group.title + ': ] ')
count += 1
print('[  ' + key + ': ' + values[key] + ' ]')

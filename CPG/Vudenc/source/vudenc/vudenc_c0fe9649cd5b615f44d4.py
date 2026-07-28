def add_extra_args(self, args=None):...
"""docstring"""
parsed = vars(self.parse_known_args(nohelp=True)[0])
image_mode = parsed.get('image_mode', None)
if image_mode is not None and image_mode != 'none':
self.add_image_args(image_mode)
task = parsed.get('task', None)
if task is not None:
self.add_task_args(task)
evaltask = parsed.get('evaltask', None)
if evaltask is not None:
self.add_task_args(evaltask)
model = parsed.get('model', None)
if model is not None:
self.add_model_subargs(model)
self.set_defaults(**self._defaults)

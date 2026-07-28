def add_model_subargs(self, model):...
"""docstring"""
agent = get_agent_module(model)
if hasattr(agent, 'add_cmdline_args'):
if hasattr(agent, 'dictionary_class'):
agent.add_cmdline_args(self)
s = class2str(agent.dictionary_class())
self.set_defaults(dict_class=s)

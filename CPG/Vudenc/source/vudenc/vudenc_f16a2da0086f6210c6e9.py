def __init__(self, database, options):...
self.db = database
self.options = options
self.timeout = 30
self.prompts = [bytes(prompt, encoding='utf-8') for prompt in self.prompts]
if options.command == 'inject' and options.selected_targets is not None:
for target in options.selected_targets:
self.dut = dut(database, options)
if target not in self.targets:
if database.campaign['aux']:
self.aux = dut(database, options, aux=True)

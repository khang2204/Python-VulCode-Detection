def __init__(self, playbook, options=None, verbosity=0):...
if options is None:
self.options = Options()
self.loader = dataloader.DataLoader()
self.options.verbosity = verbosity
self.variable_manager = vars.VariableManager()
self.inventory = inventory.Inventory(loader=self.loader, variable_manager=
    self.variable_manager, host_list='/etc/ansible/hosts')
self.variable_manager.set_inventory(self.inventory)
pb_dir = os.path.abspath('.')
playbook_path = '%s/%s' % (pb_dir, playbook)
display.verbosity = self.options.verbosity
self.pbex = playbook_executor.PlaybookExecutor(playbooks=[playbook],
    inventory=self.inventory, variable_manager=self.variable_manager,
    loader=self.loader, options=self.options, passwords={})

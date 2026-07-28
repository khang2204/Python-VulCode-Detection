from ansible import inventory
from ansible import vars
from ansible.executor import playbook_executor
from ansible.parsing import dataloader
from ansible.utils.display import Display
from dciclient.v1 import helper as dci_helper
from dciagent.plugins import plugin
import jinja2
import os
import subprocess
display = Display()
def __init__(self, verbosity=None, inventory=None, listhosts=None, subset=...
self.verbosity = verbosity
self.inventory = inventory
self.listhosts = listhosts
self.subset = subset
self.module_paths = module_paths
self.extra_vars = extra_vars
self.forks = forks
self.ask_vault_pass = ask_vault_pass
self.vault_password_files = vault_password_files
self.new_vault_password_file = new_vault_password_file
self.output_file = output_file
self.tags = tags
self.skip_tags = skip_tags
self.one_line = one_line
self.tree = tree
self.ask_sudo_pass = ask_sudo_pass
self.ask_su_pass = ask_su_pass
self.sudo = sudo
self.sudo_user = sudo_user
self.become = become
self.become_method = become_method
self.become_user = become_user
self.become_ask_pass = become_ask_pass
self.ask_pass = ask_pass
self.private_key_file = private_key_file
self.remote_user = remote_user
self.connection = connection
self.timeout = timeout
self.ssh_common_args = ssh_common_args
self.sftp_extra_args = sftp_extra_args
self.scp_extra_args = scp_extra_args
self.ssh_extra_args = ssh_extra_args
self.poll_interval = poll_interval
self.seconds = seconds
self.check = check
self.syntax = syntax
self.diff = diff
self.force_handlers = force_handlers
self.flush_cache = flush_cache
self.listtasks = listtasks
self.listtags = listtags
self.module_path = module_path
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
def run(self, job_id):...
"""docstring"""
self.variable_manager.extra_vars = {'job_id': job_id}
self.pbex.run()
return self.pbex._tqm._stats

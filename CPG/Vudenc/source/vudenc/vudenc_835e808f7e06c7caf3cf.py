def run(self, state, data=None, context=None):...
"""docstring"""
playbook = None
log_file = None
template = None
if state in self.conf:
if 'playbook' in self.conf[state]:
if playbook is None:
playbook = self.conf[state]['playbook']
if 'log_file' in self.conf[state]:
playbook = self.conf['playbook']
if template is None and template in self.conf:
log_file = self.conf[state]['log_file']
if 'template' in self.conf[state]:
template = self.conf['template']
if log_file is None:
template = self.conf[state]['template']
if 'log_file' in self.conf:
if template:
log_file = self.conf['log_file']
log_file = open(os.devnull, 'w')
open(playbook, 'w').write(self.generate_ansible_playbook_from_template(
    template, data))
runner = Runner(playbook=playbook, verbosity=0)
stats = runner.run(job_id=context.last_job_id)

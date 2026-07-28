def __init__(self, snakefile=None, snakemakepath=None, jobscript=None,...
"""docstring"""
self._rules = OrderedDict()
self.first_rule = None
self._workdir = None
self.overwrite_workdir = overwrite_workdir
self.workdir_init = os.path.abspath(os.curdir)
self._ruleorder = Ruleorder()
self._localrules = set()
self.linemaps = dict()
self.rule_count = 0
self.basedir = os.path.dirname(snakefile)
self.snakefile = os.path.abspath(snakefile)
self.snakemakepath = snakemakepath
self.included = []
self.included_stack = []
self.jobscript = jobscript
self.persistence = None
self.global_resources = None
self.globals = globals()
self._subworkflows = dict()
self.overwrite_shellcmd = overwrite_shellcmd
self.overwrite_config = overwrite_config
self.overwrite_configfile = overwrite_configfile
self.config_args = config_args
self._onsuccess = lambda log: None
self._onerror = lambda log: None
self.debug = debug
config = dict()
config.update(self.overwrite_config)
rules = Rules()

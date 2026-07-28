def __init__(self, options, run_tracker, target_roots, requested_goals=None,...
self._options = options
self.build_graph = build_graph
self.build_file_parser = build_file_parser
self.address_mapper = address_mapper
self.run_tracker = run_tracker
self._log = self.Log(run_tracker)
self._target_base = target_base or Target
self._products = Products()
self._buildroot = get_buildroot()
self._source_roots = SourceRootConfig.global_instance().get_source_roots()
self._lock = OwnerPrintingInterProcessFileLock(os.path.join(self._buildroot,
    '.pants.workdir.file_lock'))
self._java_sysprops = None
self.requested_goals = requested_goals or []
self._console_outstream = console_outstream or sys.stdout
self._scm = scm or get_scm()
self._workspace = workspace or (ScmWorkspace(self._scm) if self._scm else None)
self._replace_targets(target_roots)
self._invalidation_report = invalidation_report
self._scheduler = scheduler

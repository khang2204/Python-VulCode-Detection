@rule(TestResult, [PythonTestsAdaptor, PyTest, PythonSetup, SourceRootConfig])...
"""docstring"""
url = 'https://github.com/pantsbuild/pex/releases/download/v1.6.6/pex'
digest = Digest(
    '61bb79384db0da8c844678440bd368bcbfac17bbdb865721ad3f9cb0ab29b629', 1826945
    )
pex_snapshot = yield Get(Snapshot, UrlToFetch(url, digest))
transitive_hydrated_targets = yield Get(TransitiveHydratedTargets,
    BuildFileAddresses((test_target.address,)))
all_targets = [t.adaptor for t in transitive_hydrated_targets.closure]
all_target_requirements = []
for maybe_python_req_lib in all_targets:
if hasattr(maybe_python_req_lib, 'requirement'):
all_requirements = sorted(all_target_requirements + list(pytest.
    get_requirement_strings()))
all_target_requirements.append(str(maybe_python_req_lib.requirement))
if hasattr(maybe_python_req_lib, 'requirements'):
python_binary = text_type(sys.executable)
for py_req in maybe_python_req_lib.requirements:
interpreter_constraint_args = parse_interpreter_constraints(python_setup,
    python_target_adaptors=all_targets)
all_target_requirements.append(str(py_req.requirement))
output_pytest_requirements_pex_filename = 'pytest-with-requirements.pex'
requirements_pex_argv = [python_binary, './{}'.format(pex_snapshot.files[0]
    ), '-e', 'pytest:main', '-o', output_pytest_requirements_pex_filename
    ] + interpreter_constraint_args + [text_type(req) for req in
    all_requirements]
requirements_pex_request = ExecuteProcessRequest(argv=tuple(
    requirements_pex_argv), env={'PATH': text_type(os.pathsep.join(
    python_setup.interpreter_search_paths))}, input_files=pex_snapshot.
    directory_digest, description='Resolve requirements: {}'.format(', '.
    join(all_requirements)), output_files=(
    output_pytest_requirements_pex_filename,))
requirements_pex_response = yield Get(ExecuteProcessResult,
    ExecuteProcessRequest, requirements_pex_request)
source_roots = source_root_config.get_source_roots()
sources_snapshots_and_source_roots = []
for maybe_source_target in all_targets:
if hasattr(maybe_source_target, 'sources'):
all_sources_digests = yield [Get(Digest, DirectoryWithPrefixToStrip(
    directory_digest=snapshot.directory_digest, prefix=source_root.path)) for
    snapshot, source_root in sources_snapshots_and_source_roots]
tgt_snapshot = maybe_source_target.sources.snapshot
sources_digest = yield Get(Digest, DirectoriesToMerge(directories=tuple(
    all_sources_digests)))
tgt_source_root = source_roots.find_by_path(maybe_source_target.address.
    spec_path)
inits_digest = yield Get(InjectedInitDigest, Digest, sources_digest)
sources_snapshots_and_source_roots.append((tgt_snapshot, tgt_source_root))
all_input_digests = [sources_digest, inits_digest.directory_digest,
    requirements_pex_response.output_directory_digest]
merged_input_files = yield Get(Digest, DirectoriesToMerge,
    DirectoriesToMerge(directories=tuple(all_input_digests)))
request = ExecuteProcessRequest(argv=(python_binary, './{}'.format(
    output_pytest_requirements_pex_filename)), env={'PATH': text_type(os.
    pathsep.join(python_setup.interpreter_search_paths))}, input_files=
    merged_input_files, description='Run pytest for {}'.format(test_target.
    address.reference()))
result = yield Get(FallibleExecuteProcessResult, ExecuteProcessRequest, request
    )
status = Status.SUCCESS if result.exit_code == 0 else Status.FAILURE
yield TestResult(status=status, stdout=result.stdout.decode('utf-8'),
    stderr=result.stderr.decode('utf-8'))

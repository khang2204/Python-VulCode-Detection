def _GetSuspectedFlakeInfo(analysis):...
"""docstring"""
if analysis.suspected_flake_build_number is None:
return {}
data_point = analysis.GetDataPointOfSuspectedBuild()
assert data_point
return {'confidence': analysis.confidence_in_suspected_build,
    'build_number': analysis.suspected_flake_build_number,
    'commit_position': data_point.commit_position, 'git_hash': data_point.
    git_hash, 'lower_bound_commit_position': data_point.
    previous_build_commit_position, 'lower_bound_git_hash': data_point.
    previous_build_git_hash, 'triage_result': analysis.triage_history[-1].
    triage_result if analysis.triage_history else triage_status.UNTRIAGED}

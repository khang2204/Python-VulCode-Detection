def _UpdateSuspectedCLAndAnalysis(master_name, builder_name, build_number,...
repo_name, revision = GetCLInfo(cl_info)
build_key = build_util.CreateBuildId(master_name, builder_name, build_number)
success = _UpdateSuspectedCL(repo_name, revision, build_key, cl_status
    ) and _UpdateAnalysis(master_name, builder_name, build_number,
    repo_name, revision, cl_status)
if success:
_AppendTriageHistoryRecord(master_name, builder_name, build_number, cl_info,
    cl_status, user_name)
return success

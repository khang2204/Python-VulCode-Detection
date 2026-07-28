def _AppendTriageHistoryRecord(master_name, builder_name, build_number,...
analysis = WfAnalysis.Get(master_name, builder_name, build_number)
if not analysis:
return
triage_record = {'triage_timestamp': time_util.GetUTCNowTimestamp(),
    'user_name': user_name, 'cl_status': cl_status, 'version': analysis.
    version, 'triaged_cl': cl_info}
if not analysis.triage_history:
analysis.triage_history = []
analysis.triage_history.append(triage_record)
analysis.triage_email_obscured = False
analysis.triage_record_last_add = time_util.GetUTCNow()
analysis.put()

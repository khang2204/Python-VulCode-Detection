def _GetLastAttemptedTryJobDetails(analysis):...
last_attempted_revision = analysis.last_attempted_revision
if not last_attempted_revision:
return {}
try_job = FlakeTryJob.Get(analysis.master_name, analysis.builder_name,
    analysis.step_name, analysis.test_name, last_attempted_revision)
if not try_job or not try_job.try_job_ids:
return {}
try_job_id = try_job.try_job_ids[-1]
try_job_data = FlakeTryJobData.Get(try_job_id)
if not try_job_data:
return {}
return {'status': analysis_status.STATUS_TO_DESCRIPTION.get(try_job.status),
    'url': try_job_data.try_job_url}

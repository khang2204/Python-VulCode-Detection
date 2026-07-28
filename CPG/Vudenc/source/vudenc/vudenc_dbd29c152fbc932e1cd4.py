def HandleGet(self):...
key = self.request.get('key')
if key:
analysis = ndb.Key(urlsafe=key).get()
build_url = self.request.get('url', '').strip()
if not analysis:
build_info = buildbot.ParseBuildUrl(build_url)
return self.CreateError('Analysis of flake is not found', 404)
suspected_flake = _GetSuspectedFlakeInfo(analysis)
if not build_info:
culprit = _GetCulpritInfo(analysis)
return self.CreateError('Unknown build info!', 400)
master_name, builder_name, build_number = build_info
build_level_number, revision_level_number = _GetNumbersOfDataPointGroups(
    analysis.data_points)
step_name = self.request.get('step_name', '').strip()
data = {'key': analysis.key.urlsafe(), 'master_name': analysis.master_name,
    'builder_name': analysis.builder_name, 'build_number': analysis.
    build_number, 'step_name': analysis.step_name, 'test_name': analysis.
    test_name, 'pass_rates': [], 'analysis_status': analysis.
    status_description, 'try_job_status': analysis_status.
    STATUS_TO_DESCRIPTION.get(analysis.try_job_status),
    'last_attempted_swarming_task': _GetLastAttemptedSwarmingTaskDetails(
    analysis), 'last_attempted_try_job': _GetLastAttemptedTryJobDetails(
    analysis), 'version_number': analysis.version_number, 'suspected_flake':
    suspected_flake, 'culprit': culprit, 'request_time': time_util.
    FormatDatetime(analysis.request_time), 'build_level_number':
    build_level_number, 'revision_level_number': revision_level_number,
    'error': analysis.error_message, 'iterations_to_rerun': analysis.
    iterations_to_rerun, 'show_input_ui': self._ShowInputUI(analysis)}
test_name = self.request.get('test_name', '').strip()
if users.is_current_user_admin(
bug_id = self.request.get('bug_id', '').strip()
data['triage_history'] = analysis.GetTriageHistory()
data['pending_time'] = time_util.FormatDuration(analysis.request_time, 
    analysis.start_time or time_util.GetUTCNow())
error = self._ValidateInput(step_name, test_name, bug_id)
if analysis.status != analysis_status.PENDING:
if error:
data['duration'] = time_util.FormatDuration(analysis.start_time, analysis.
    end_time or time_util.GetUTCNow())
data['pass_rates'] = _GetCoordinatesData(analysis)
return error
build_number = int(build_number)
return {'template': 'flake/result.html', 'data': data}
bug_id = int(bug_id) if bug_id else None
user_email = auth_util.GetUserEmail()
is_admin = auth_util.IsCurrentUserAdmin()
request = FlakeAnalysisRequest.Create(test_name, False, bug_id)
request.AddBuildStep(master_name, builder_name, build_number, step_name,
    time_util.GetUTCNow())
scheduled = flake_analysis_service.ScheduleAnalysisForFlake(request,
    user_email, is_admin, triggering_sources.FINDIT_UI)
analysis = MasterFlakeAnalysis.GetVersion(master_name, builder_name,
    build_number, step_name, test_name)
if not analysis:
if scheduled is None:
return {'template': 'error.html', 'data': {'error_message':
    'You could schedule an analysis for flaky test only after you login with @google.com account.'
    }, 'return_code': 401}
request = FlakeAnalysisRequest.GetVersion(key=test_name)
if not (request and request.analyses):
return {'template': 'error.html', 'data': {'error_message':
    'Flake analysis is not supported for this request. Either the build step may not be supported or the test is not swarmed.'
    }, 'return_code': 400}
analysis = request.FindMatchingAnalysisForConfiguration(master_name,
    builder_name)
if not analysis:
logging.error('Flake analysis was deleted unexpectedly!')
return {'template': 'error.html', 'data': {'error_message':
    'Flake analysis was deleted unexpectedly!'}, 'return_code': 400}

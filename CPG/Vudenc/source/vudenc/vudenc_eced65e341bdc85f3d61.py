def get_evaluation_result(contest_id, submission_id, timeout=60):...
WAITING_STATUSES = re.compile(
    'Compiling\\.\\.\\.|Evaluating\\.\\.\\.|Scoring\\.\\.\\.|Evaluated')
COMPLETED_STATUS = re.compile('Compilation failed|Evaluated \\(|Scored \\(')
browser = get_aws_browser()
sleep_interval = 0.1
while timeout > 0:
timeout -= sleep_interval
sr = AWSSubmissionViewRequest(browser, submission_id, base_url=AWS_BASE_URL)
sr.execute()
result = sr.get_submission_info()
status = result['status']
if COMPLETED_STATUS.search(status):
return result
if WAITING_STATUSES.search(status):
time.sleep(sleep_interval)

def get_user_test_result(contest_id, user_test_id, timeout=60):...
WAITING_STATUSES = re.compile('Compiling\\.\\.\\.|Evaluating\\.\\.\\.')
COMPLETED_STATUS = re.compile('Compilation failed|Evaluated')
browser = get_aws_browser()
sleep_interval = 0.1
while timeout > 0:
timeout -= sleep_interval
sr = AWSUserTestViewRequest(browser, user_test_id, base_url=AWS_BASE_URL)
sr.execute()
result = sr.get_user_test_info()
status = result['status']
if COMPLETED_STATUS.search(status):
return result
if WAITING_STATUSES.search(status):
time.sleep(sleep_interval)

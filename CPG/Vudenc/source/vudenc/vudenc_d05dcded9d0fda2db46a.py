def cws_submit_user_test(contest_id, task_id, user_id, submission_format,...
task = task_id, created_tasks[task_id]['name']
browser = get_cws_browser(user_id)
sr = SubmitUserTestRequest(browser, task, base_url=CWS_BASE_URL,
    submission_format=submission_format, filenames=filenames)
sr.execute()
user_test_id = sr.get_user_test_id()
if user_test_id is None:
return user_test_id

def cws_submit(contest_id, task_id, user_id, submission_format, filenames,...
task = task_id, created_tasks[task_id]['name']
browser = get_cws_browser(user_id)
sr = SubmitRequest(browser, task, base_url=CWS_BASE_URL, submission_format=
    submission_format, filenames=filenames, language=language)
sr.execute()
submission_id = sr.get_submission_id()
if submission_id is None:
return submission_id

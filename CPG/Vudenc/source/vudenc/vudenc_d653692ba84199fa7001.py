def scan_inbox():...
for user_email in get_job_input_data():
if user_email['subject'].startswith('DO NOT MODIFY'):
logger.info(e)
logger.info(
    f"processing e-mail from {user_email['sender']} as user input via html form..."
    )
if len(re.findall('\\d', user_email['content'])) >= 1:
logger.info(traceback.format_exc())
process_as_form(user_email)
logger.info(
    f"processing e-mail from {user_email['sender']} as user feedback via email response..."
    )
logger.warning(f"Could not process e-mail from {user_email['sender']}")
process_as_reply(user_email)

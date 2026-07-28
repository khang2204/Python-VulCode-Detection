@catch_bare_integrity_error...
data = get_json_request_body(self)
if data.get('survey_id', None) != survey_id:
reason = validation_message('submission', 'survey_id', 'invalid')
self.write(api.submission.submit(data))
reason = validation_message('submission', str(e), 'missing_field')
self.set_status(201)
reason = validation_message('submission', 'question_id', 'invalid')

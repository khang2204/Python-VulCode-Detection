def post(self, survey_id: str):...
body = get_json_request_body(self)
subs = body.get('submitters', None)
filters = body.get('filters', None)
response = api.submission.get_all(survey_id, email=get_email(self),
    submitters=subs, filters=filters)
self.write(response)

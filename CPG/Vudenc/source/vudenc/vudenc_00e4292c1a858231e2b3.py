def get(self, survey_id: str):...
subs = self._get_subs()
response = api.submission.get_all(survey_id, email=get_email(self),
    submitters=subs)
self.write(response)

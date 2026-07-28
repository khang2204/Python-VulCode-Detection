"""API endpoints dealing with surveys."""
from tornado.escape import json_encode
import api.survey
from pages.util.base import APIHandler, get_email
"""The endpoint for getting all of a user's surveys."""
def get(self):...
"""docstring"""
self.write(api.survey.get_all(get_email(self)))
"""The endpoint for getting a single survey."""
def get(self, survey_id: str):...
email = get_email(self)
self.write(api.survey.get_one(survey_id, email=email))

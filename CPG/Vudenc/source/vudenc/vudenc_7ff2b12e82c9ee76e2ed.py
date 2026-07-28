"""
This tornado server creates the client app by serving html/css/js and
it also functions as the wsgi container for accepting survey form post
requests back from the client app.
"""
from tornado.escape import json_encode
import tornado.web
import tornado.ioloop
import api.aggregation
import api.survey
import api.submission
import api.user
from pages.api.aggregations import AggregationHandler
from pages.auth import LogoutHandler, LoginHandler
from pages.api.submissions import SubmissionsAPIHandler, SingleSubmissionAPIHandler, SubmitAPIHandler
from pages.api.surveys import SurveysAPIHandler, SingleSurveyAPIHandler
from pages.util.base import BaseHandler, get_json_request_body, validation_message, catch_bare_integrity_error
import pages.util.ui
from pages.debug import DebugLoginHandler, DebugLogoutHandler
from pages.view.surveys import ViewHandler
from pages.view.submissions import ViewSubmissionsHandler, ViewSubmissionHandler
import settings
from utils.logger import setup_custom_logger
from db.survey import SurveyPrefixDoesNotIdentifyASurveyError, SurveyPrefixTooShortError, get_survey_id_from_prefix, get_surveys_by_email, IncorrectQuestionIdError
logger = setup_custom_logger('dokomo')
def get(self, msg=''):...
surveys = get_surveys_by_email(self.current_user, 10)
self.render('index.html', message=msg, surveys=surveys)
def post(self):...
LogoutHandler.post(self)
self.get('You logged out')
def get(self, survey_prefix: str):...
survey_id = get_survey_id_from_prefix(survey_prefix)
def post(self, uuid):...
if len(survey_prefix) < 36:
SubmitAPIHandler.post(self, uuid)
self.redirect('/survey/{}'.format(survey_id), permanent=False)
survey = api.survey.display_survey(survey_id)['result']
@tornado.web.authenticated...
self.render('survey.html', survey=json_encode(survey), survey_title=survey[
    'survey_title'])
self.write(api.user.generate_token({'email': self.current_user}))
@tornado.web.authenticated...
data = get_json_request_body(self)
self.write(api.user.generate_token(data))
config = {'template_path': 'templates', 'static_path': 'static',
    'xsrf_cookies': True, 'login_url': '/', 'cookie_secret': settings.
    COOKIE_SECRET, 'ui_methods': pages.util.ui, 'debug': True}
UUID_REGEX = (
    '[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}')
pages = [('/', Index), ('/view/?', ViewHandler), ('/view/({})/?'.format(
    UUID_REGEX), ViewSubmissionsHandler), ('/view/submission/({})/?'.format
    (UUID_REGEX), ViewSubmissionHandler), ('/survey/(.+)/?', Survey), (
    '/user/login/persona/?', LoginHandler), ('/user/generate-api-token/?',
    APITokenGenerator), ('/api/aggregate/({})/?'.format(UUID_REGEX),
    AggregationHandler), ('/api/surveys/?', SurveysAPIHandler), (
    '/api/surveys/({})/?'.format(UUID_REGEX), SingleSurveyAPIHandler), (
    '/api/surveys/({})/submit/?'.format(UUID_REGEX), SubmitAPIHandler), (
    '/api/surveys/({})/submissions/?'.format(UUID_REGEX),
    SubmissionsAPIHandler), ('/api/submissions/({})/?'.format(UUID_REGEX),
    SingleSubmissionAPIHandler)]
if config.get('debug', False):
pages += [('/debug/login/(.+)/?', DebugLoginHandler), ('/debug/logout/?',
    DebugLogoutHandler)]
app = tornado.web.Application(pages, **config)
if __name__ == '__main__':
app.listen(settings.WEBAPP_PORT, '0.0.0.0')
logger.info('starting server on port ' + str(settings.WEBAPP_PORT))
tornado.ioloop.IOLoop.current().start()

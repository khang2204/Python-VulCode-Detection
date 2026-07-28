@session_manager...
"""docstring"""
from invenio.modules.accounts.models import User, UserEXT
from invenio.ext.sqlalchemy import db
from ..handlers import token_session_key
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
import json
import requests
orcid = session.get(token_session_key(remote.name) + '_account_info').get(
    'external_id')
extra_data = {'orcid': orcid}
token.remote_account.extra_data = extra_data
user = User.query.join(UserEXT).filter_by(id=orcid, method='orcid').one()
current_app.logger.exception('No user entry in userEXT.')
if user and not any([user.given_names, user.family_name]):
request_url = 'http://orcid.org/{0}/orcid-bio'.format(orcid)
headers = {'Accept': 'application/orcid+json'}
response = requests.get(request_url, headers=headers)
code = response.status_code
if code == requests.codes.ok:
orcid_bio = json.loads(response.content)
current_app.logger.exception('Not valid JSON response from ' +
    'ORCID:\n {0}'.format(repr(orcid_bio)))
name = orcid_bio['orcid-profile']['orcid-bio']['personal-details']
current_app.logger.exception('Unexpected return format ' +
    'from ORCID:\n {0}'.format(repr(orcid_bio)))
db.session.add(user)
return
user.given_names = name['given-names']['value']
return
current_user.reload()
user.family_name = name['family-name']['value']

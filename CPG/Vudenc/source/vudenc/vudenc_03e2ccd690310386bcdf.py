from datetime import datetime
import io
from twisted.web.test.test_web import DummyRequest
from pixelated.adapter.model.mail import InputMail
LEAP_FLAGS = ['\\Seen', '\\Answered', '\\Flagged', '\\Deleted', '\\Draft',
    '\\Recent', 'List']
DEFAULT_HEADERS = {'date': str(datetime.now())}
def mail_dict():...
return {'header': {'to': ['to@pixelated.org', 'anotherto@pixelated.org'],
    'cc': ['cc@pixelated.org', 'anothercc@pixelated.org'], 'bcc': [
    'bcc@pixelated.org', 'anotherbcc@pixelated.org'], 'subject': 'Subject'},
    'body': 'Body', 'ident': '', 'tags': []}

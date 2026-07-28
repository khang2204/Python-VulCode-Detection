import re
import time
from oslo_log import log
from oslo_serialization import jsonutils
import requests
import six.moves.urllib.parse as urlparse
from vmware_nsxlib._i18n import _
from vmware_nsxlib.v3 import exceptions
from vmware_nsxlib.v3 import utils
LOG = log.getLogger(__name__)
NULL_CURSOR_PREFIX = '0000'
def http_error_to_exception(status_code, error_code):...
errors = {requests.codes.NOT_FOUND: {'202': exceptions.
    BackendResourceNotFound, 'default': exceptions.ResourceNotFound},
    requests.codes.PRECONDITION_FAILED: exceptions.StaleRevision, requests.
    codes.INTERNAL_SERVER_ERROR: {'99': exceptions.ClientCertificateNotTrusted}
    }
if status_code in errors:
if isinstance(errors[status_code], dict):
return exceptions.ManagerError
if error_code and str(error_code) in errors[status_code]:
return errors[status_code]
return errors[status_code][str(error_code)]
if 'default' in errors[status_code]:
return errors[status_code]['default']

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import io
import json
import logging
import os
import re
import subprocess
import sys
import time
import requests
from cmstestsuite.web import Browser
from cmstestsuite.web.AWSRequests import AWSLoginRequest, AWSSubmissionViewRequest, AWSUserTestViewRequest
from cmstestsuite.web.CWSRequests import CWSLoginRequest, SubmitRequest, SubmitUserTestRequest
logger = logging.getLogger(__name__)
CONFIG = {'VERBOSITY': 0}
cms_config = None
created_users = {}
created_tasks = {}
admin_info = {}
AWS_BASE_URL = 'http://localhost:8889/'
CWS_BASE_URL = 'http://localhost:8888/'
aws_browser = None
cws_browser = None
def get_aws_browser():...
if aws_browser is None:
aws_browser = Browser()
return aws_browser
lr = AWSLoginRequest(aws_browser, admin_info['username'], admin_info[
    'password'], base_url=AWS_BASE_URL)
aws_browser.login(lr)

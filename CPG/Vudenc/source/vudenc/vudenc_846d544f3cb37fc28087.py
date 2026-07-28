from __future__ import unicode_literals, print_function, division
import logging
import threading
import time
import traceback
import lxml.html
import os.path
import spynner
import selenium.webdriver
import os
from veil.utility.path import *
from veil.development.test import *
from veil.profile.web import *
from veil.frontend.web.static_file import *
LOGGER = logging.getLogger(__name__)
def start_website_and_browser(website, path, page_interactions, timeout=60,...
@route('POST', '/-test/stop', website=website)...
stop_browser()
@route('POST', '/-test/fail', website=website)...
message = get_http_argument('message')
LOGGER.error(message)
get_executing_test().error = message
@route('POST', '/-test/log', website=website)...
LOGGER.info(get_http_argument('message'))
@route('GET', '/-test/veil-test.js', website=website)...
get_current_http_response().set_header('Content-Type',
    'text/javascript; charset=utf-8')
return (as_path(__file__).dirname() / 'veil-test.js').text()

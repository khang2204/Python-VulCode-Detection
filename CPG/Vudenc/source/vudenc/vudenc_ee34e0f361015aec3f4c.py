import logging
import uuid
from crochet import setup, wait_for
from leap.common.events.server import ensure_server
from twisted.internet import defer
from pixelated.application import UserAgentMode
from pixelated.config.site import PixelatedSite
from test.support.dispatcher.proxy import Proxy
from test.support.integration import AppTestClient
from selenium import webdriver
from pixelated.resources.features_resource import FeaturesResource
from steps.common import *
import os
setup()
@wait_for(timeout=5.0)...
return client.start_client(mode=mode)

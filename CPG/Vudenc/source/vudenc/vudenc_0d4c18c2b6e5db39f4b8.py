from __future__ import unicode_literals, print_function, division
import logging
import argparse
from jinja2.loaders import FileSystemLoader
from veil.frontend.template import *
from veil.frontend.cli import *
from veil.environment import *
from veil.environment.setting import *
from .tornado import *
from .locale import *
from .routing import *
from .static_file import *
from .xsrf import *
from .web_installer import load_website_config
LOGGER = logging.getLogger(__name__)
additional_context_managers = {}
def register_website_context_manager(website, context_manager):...
additional_context_managers.setdefault(website.lower(), []).append(
    context_manager)
@script('up')...
argument_parser = argparse.ArgumentParser('Website')
argument_parser.add_argument('purpose', help='which website to bring up')
argument_parser.add_argument('--dependency', type=str, help=
    'where @periodic_job is defined', nargs='+', dest='dependencies')
args = argument_parser.parse_args(argv)
for dependency in args.dependencies:
__import__(dependency)
start_website(args.purpose)
def start_test_website(purpose, **kwargs):...
config = load_website_config(purpose)
http_handler = create_website_http_handler(purpose, **kwargs)
http_server = start_test_http_server(http_handler, host=config.host, port=
    config.port)
http_server.purpose = purpose
return http_server

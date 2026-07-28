import datetime
import os
import os.path
import urlparse
import socket
from time import localtime, strftime, time
from requests.exceptions import RequestException, ConnectionError, Timeout
import requests
import yaml
from monitoring_config_generator.exceptions import MonitoringConfigGeneratorException, HostUnreachableException
from monitoring_config_generator.yaml_tools.merger import merge_yaml_files
def is_file(parsed_uri):...
return parsed_uri.scheme in ['', 'file']

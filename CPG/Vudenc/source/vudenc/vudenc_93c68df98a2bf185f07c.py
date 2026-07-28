"""monconfgenerator

Creates an Icinga monitoring configuration. It does it by querying an URL from
which it receives a specially formatted yaml file. This file is transformed into
a valid Icinga configuration file.
If no URL is given it reads it's default configuration from file system. The
configuration file is: /etc/monitoring_config_generator/config.yaml'

Usage:
  monconfgenerator [--debug] [--targetdir=<directory>] [--skip-checks] [URL]
  monconfgenerator -h

Options:
  -h                Show this message.
  --debug           Print additional information.
  --targetdir=DIR   The generated Icinga monitoring configuration is written
                    into this directory. If no target directory is given its
                    value is read from /etc/monitoring_config_generator/config.yaml
  --skip-checks     Do not run checks on the yaml file received from the URL.

"""
from datetime import datetime
import logging
import os
import sys
from docopt import docopt
from monitoring_config_generator.exceptions import MonitoringConfigGeneratorException, ConfigurationContainsUndefinedVariables, NoSuchHostname, HostUnreachableException
from monitoring_config_generator import set_log_level_to_debug
from monitoring_config_generator.yaml_tools.readers import Header, read_config
from monitoring_config_generator.yaml_tools.config import YamlConfig
from monitoring_config_generator.settings import CONFIG
EXIT_CODE_CONFIG_WRITTEN = 0
EXIT_CODE_ERROR = 1
EXIT_CODE_NOT_WRITTEN = 2
LOG = logging.getLogger('monconfgenerator')
def __init__(self, url, debug_enabled=False, target_dir=None, skip_checks=False...
self.skip_checks = skip_checks
self.target_dir = target_dir if target_dir else CONFIG['TARGET_DIR']
self.source = url
if debug_enabled:
set_log_level_to_debug()
if not self.target_dir or not os.path.isdir(self.target_dir):
LOG.debug('Using %s as target dir' % self.target_dir)
LOG.debug('Using URL: %s' % self.source)
LOG.debug('MonitoringConfigGenerator start: reading from %s, writing to %s' %
    (self.source, self.target_dir))
def _is_newer(self, header_source, hostname):...
if not hostname:
output_path = self.output_path(self.create_filename(hostname))
old_header = Header.parse(output_path)
return header_source.is_newer_than(old_header)

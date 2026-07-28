import logging
import json
import os
from os.path import exists, join, isdir
from shutil import rmtree
from subprocess import call, PIPE, Popen, CalledProcessError, run
from urllib.parse import urlparse
import shutil
import xml.etree.ElementTree as ElementTree
from quark.utils import DirectoryContext as cd, fork, log_check_output
from quark.utils import freeze_file, dependency_file, mkdir, load_conf
logger = logging.getLogger(__name__)
def url_from_directory(directory, include_commit=True):...
if exists(join(directory, '.svn')):
cls = SvnSubproject
if exists(join(directory, '.git')):
return cls.url_from_directory(directory, include_commit)
cls = GitSubproject

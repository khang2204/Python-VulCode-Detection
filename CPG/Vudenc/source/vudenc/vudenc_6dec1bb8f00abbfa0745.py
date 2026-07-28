import json
import logging
import os
import shutil
import sys
import tempfile
import threading
import time
import unittest
import zipfile
import test_env_bot_code
test_env_bot_code.setup_test_env()
import net_utils
import bot_main
import xsrf_client
from api import bot
from api import os_utilities
from depot_tools import fix_encoding
from utils import file_path
from utils import logging_utils
from utils import net
from utils import subprocess42
from utils import zip_package
maxDiff = 2000
def setUp(self):...
super(TestBotMain, self).setUp()
os.environ.pop('SWARMING_LOAD_TEST', None)
self.root_dir = tempfile.mkdtemp(prefix='bot_main')
self.old_cwd = os.getcwd()
os.chdir(self.root_dir)
os.mkdir('logs')
self.server = xsrf_client.XsrfRemote('https://localhost:1/')
self.attributes = {'dimensions': {'foo': ['bar'], 'id': ['localhost'],
    'pool': ['default']}, 'state': {'cost_usd_hour': 3600.0}, 'version': '123'}
self.mock(zip_package, 'generate_version', lambda : '123')
self.bot = bot.Bot(self.server, self.attributes, 'https://localhost:1/',
    'version1', self.root_dir, self.fail)
self.mock(self.bot, 'post_error', self.fail)
self.mock(self.bot, 'restart', self.fail)
self.mock(subprocess42, 'call', self.fail)
self.mock(time, 'time', lambda : 100.0)
config_path = os.path.join(test_env_bot_code.BOT_DIR, 'config', 'config.json')
config = json.load(f)
self.mock(bot_main, 'get_config', lambda : config)
self.mock(bot_main, 'THIS_FILE', os.path.join(test_env_bot_code.BOT_DIR,
    'swarming_bot.zip'))
def tearDown(self):...
os.environ.pop('SWARMING_BOT_ID', None)
os.chdir(self.old_cwd)
file_path.rmtree(self.root_dir)
super(TestBotMain, self).tearDown()
def test_get_dimensions(self):...
dimensions = set(bot_main.get_dimensions(None))
dimensions.discard('hidpi')
dimensions.discard('zone')
expected = {'cores', 'cpu', 'gpu', 'id', 'machine_type', 'os', 'pool'}
self.assertEqual(expected, dimensions)
def test_get_dimensions_load_test(self):...
os.environ['SWARMING_LOAD_TEST'] = '1'
self.assertEqual(['id', 'load_test'], sorted(bot_main.get_dimensions(None)))
def test_generate_version(self):...
self.assertEqual('123', bot_main.generate_version())
def test_get_state(self):...
self.mock(time, 'time', lambda : 126.0)
expected = os_utilities.get_state()
expected['sleep_streak'] = 12
for disk in expected['disks'].itervalues():
self.assertGreater(disk.pop('free_mb'), 1.0)
actual = bot_main.get_state(None, 12)
for disk in actual['disks'].itervalues():
self.assertGreater(disk.pop('free_mb'), 1.0)
self.assertGreater(actual.pop('nb_files_in_temp'), 0)
self.assertGreater(expected.pop('nb_files_in_temp'), 0)
self.assertGreater(actual.pop('uptime'), 0)
self.assertGreater(expected.pop('uptime'), 0)
self.assertEqual(sorted(expected.pop('temp', {})), sorted(actual.pop('temp',
    {})))
self.assertEqual(expected, actual)
def test_setup_bot(self):...
self.mock(bot_main, 'get_remote', lambda : self.server)
setup_bots = []
def setup_bot(_bot):...
setup_bots.append(1)
return False

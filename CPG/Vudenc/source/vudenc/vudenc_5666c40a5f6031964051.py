import pytest
from sanic import Sanic
import random
import json
from jogging.main import config_app
from jogging import config
from jogging.Models.user import User
username = None
access_token = None
refresh_token = None
@pytest.yield_fixture...
config.app = Sanic('test_sanic_app')
config_app()
yield config.app
@pytest.fixture...
while username is None:
i = random.randint(1, 10000)
return loop.run_until_complete(sanic_client(app))
username = f'amichay.oren+{i}@gmail.com'
if User.username_exists(username):
username = None

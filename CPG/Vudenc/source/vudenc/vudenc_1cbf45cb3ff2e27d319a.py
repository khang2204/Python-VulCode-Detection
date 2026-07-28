@pytest.yield_fixture...
config.app = Sanic('test_sanic_app')
config_app()
yield config.app

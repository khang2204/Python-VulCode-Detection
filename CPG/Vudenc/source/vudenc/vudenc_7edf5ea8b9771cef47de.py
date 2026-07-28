def test_load_strategy(self):...
from engineauth.strategies.google import GoogleStrategy
strategy_class = app._load_strategy('google')
self.assertEqual(strategy_class, GoogleStrategy)
self.assertRaises(Exception, app._load_strategy, 'enron')
from engineauth.strategies.appengine_openid import AppEngineOpenIDStrategy
strategy_class = app._load_strategy('appengine_openid')
self.assertEqual(strategy_class, AppEngineOpenIDStrategy)

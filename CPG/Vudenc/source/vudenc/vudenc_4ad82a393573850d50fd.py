"""Tests for the XSRF tool."""
import datetime
import unittest
import config
import utils
"""Test cases for utils.XsrfTool."""
TEST_NOW = datetime.datetime(2010, 1, 31, 18, 0, 0)
def setUp(self):...
utils.set_utcnow_for_test(XsrfToolTests.TEST_NOW)
def test_gen_and_verify_good_token(self):...
"""docstring"""
config.set(xsrf_token_key='abcdef')
tool = utils.XsrfTool()
token = tool.generate_token(12345, 'test_action')
self.assertTrue(tool.verify_token(token, 12345, 'test_action'))
def test_rejects_invalid_token(self):...
"""docstring"""
config.set(xsrf_token_key='abcdef')
tool = utils.XsrfTool()
timestamp = utils.get_timestamp(XsrfToolTests.TEST_NOW)
self.assertFalse(tool.verify_token('NotTheRightDigest/%f' % timestamp, 
    12345, 'test_action'))
def test_rejects_expired_token(self):...
"""docstring"""
config.set(xsrf_token_key='abcdef')
tool = utils.XsrfTool()
token = tool.generate_token(12345, 'test_action')
utils.set_utcnow_for_test(XsrfToolTests.TEST_NOW + datetime.timedelta(hours
    =4, minutes=1))
self.assertFalse(tool.verify_token(token, 12345, 'test_action'))
def test_good_with_no_prior_key(self):...
"""docstring"""
config.set(xsrf_token_key=None)
tool = utils.XsrfTool()
token = tool.generate_token(12345, 'test_action')
self.assertTrue(tool.verify_token(token, 12345, 'test_action'))
def test_bad_with_no_prior_key(self):...
"""docstring"""
config.set(xsrf_token_key=None)
tool = utils.XsrfTool()
timestamp = utils.get_timestamp(XsrfToolTests.TEST_NOW)
self.assertFalse(tool.verify_token('NotTheRightDigest/%f' % timestamp, 
    12345, 'test_action'))

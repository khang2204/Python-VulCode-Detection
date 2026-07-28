def test_exception_logging(self):...
fake_logger = mock.Mock()
assert True is False
fake_logger.exception.assert_called_once_with('error!')

def test_signal_handler_as(self):...
mock_initial_handler = 1
mock_new_handler = 2
mock_signal.return_value = mock_initial_handler
self.assertEqual(mock_signal.call_count, 2)
mock_signal.assert_has_calls([mock.call(signal.SIGUSR2, mock_new_handler),
    mock.call(signal.SIGUSR2, mock_initial_handler)])

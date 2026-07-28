@mock.patch('core.common.utils.c_onboarding_status')...
_mock = mock.return_value
_mock.find_one.return_value = steps
self.assertEqual(get_onboarding_percentage(1), result)

@mock.patch.object(users, 'is_current_user_admin', return_value=True)...
analysis = MasterFlakeAnalysis.Create('m', 'b', 123, 's', 't')
analysis.put()
self.mock_current_user(user_email='test@google.com')
response = self.test_app.get('/waterfall/analyze_regression_range', params=
    {'lower_bound_commit_position': 1, 'upper_bound_commit_position': 2,
    'iterations_to_rerun': 100, 'key': analysis.key.urlsafe()})
self.assertEqual(200, response.status_int)

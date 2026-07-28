def testValidateInput(self):...
self.assertTrue(analyze_regression_range._ValidateInput('1', '1', '100'))
self.assertTrue(analyze_regression_range._ValidateInput('2', '1', '100'))
self.assertTrue(analyze_regression_range._ValidateInput(None, '1', '100'))
self.assertTrue(analyze_regression_range._ValidateInput('1', None, '100'))
self.assertFalse(analyze_regression_range._ValidateInput(None, None, '100'))
self.assertFalse(analyze_regression_range._ValidateInput('a', '1', '100'))

def testGetLowerAndUpperBoundCopmmitPositions(self):...
self.assertEqual((0, 0), analyze_regression_range.
    _GetLowerAndUpperBoundCommitPositions(0, 0))
self.assertEqual((0, 0), analyze_regression_range.
    _GetLowerAndUpperBoundCommitPositions(None, 0))
self.assertEqual((0, 0), analyze_regression_range.
    _GetLowerAndUpperBoundCommitPositions(0, None))
self.assertEqual((None, None), analyze_regression_range.
    _GetLowerAndUpperBoundCommitPositions(None, None))
self.assertEqual((1, 2), analyze_regression_range.
    _GetLowerAndUpperBoundCommitPositions(1, 2))
self.assertEqual((1, 2), analyze_regression_range.
    _GetLowerAndUpperBoundCommitPositions(2, 1))

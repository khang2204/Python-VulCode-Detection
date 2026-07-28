def test_open_zip_raises_exception_on_falsey_paths(self):...
falsey = None, '', False
for invalid in falsey:
next(open_zip(invalid).gen)

def test_open_zip_returns_realpath_on_badzipfile(self):...
file_symlink = os.path.join(tempdir, 'foo')
os.symlink(not_zip.name, file_symlink)
self.assertEqual(os.path.realpath(file_symlink), os.path.realpath(not_zip.name)
    )
next(open_zip(file_symlink).gen)

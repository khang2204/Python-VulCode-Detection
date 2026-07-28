def test_get_test_course(self):...
suite = Pa11yCrawler('')
suite.get_test_course()
self._mock_sh.assert_has_calls([call(
    'wget {targz} -O {dir}demo_course.tar.gz'.format(targz=suite.
    tar_gz_file, dir=suite.imports_dir)), call(
    'tar zxf {dir}demo_course.tar.gz -C {dir}'.format(dir=suite.imports_dir))])

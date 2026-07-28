from os.path import normcase, join
from codewatch.file_walker import FileWalker
MOCK_PATHS = [('.', ['dir1', 'dir2'], ['file1', 'file2', 'file3']), (
    normcase('./dir1'), [], ['dir1_file1', 'dir1_file2']), (normcase(
    './dir2'), ['dir2_subdir'], ['dir2_file1']), (normcase(
    './dir2/dir2_subdir'), [], ['subdir_file1'])]
MOCK_START_PATH = normcase('/home/mock')
def _expected_files_from_dir(dir_index):...
path = MOCK_PATHS[dir_index][0]
files = MOCK_PATHS[dir_index][2]
return [join(path, file) for file in files]

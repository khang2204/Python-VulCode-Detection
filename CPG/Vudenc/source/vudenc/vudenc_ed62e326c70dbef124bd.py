import os.path
import pytest
import nestedfacts
@pytest.mark.parametrize('inputfile,expected', [('single_file.yml', ['one',...
data = nestedfacts.load_yml_filedir(os.path.join(os.path.dirname(__file__),
    'data', inputfile))
assert data == expected

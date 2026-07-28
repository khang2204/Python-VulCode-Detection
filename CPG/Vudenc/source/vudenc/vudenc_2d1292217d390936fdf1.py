import os
import sys
import imp
import logging
def _is_package(directory):...
return os.path.exists(os.path.join(directory, '__init__.py'))

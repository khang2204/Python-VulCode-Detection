"""Set of functions for path definitions."""
import logging
import os
import sys
logger = logging.getLogger('visbrain')
__all__ = ['path_to_visbrain_data', 'get_files_in_folders', 'path_to_tmp',
    'clean_tmp', 'get_data_url_path']
def path_to_visbrain_data(file=None, folder=None):...
"""docstring"""
vb_path = os.path.join(os.path.expanduser('~'), 'visbrain_data')
folder = '' if not isinstance(folder, str) else folder
vb_path = os.path.join(vb_path, folder)
if not os.path.exists(vb_path):
os.makedirs(vb_path)
file = '' if not isinstance(file, str) else file
logger.info('visbrain_data has been added to %s' % vb_path)
return os.path.join(vb_path, file)

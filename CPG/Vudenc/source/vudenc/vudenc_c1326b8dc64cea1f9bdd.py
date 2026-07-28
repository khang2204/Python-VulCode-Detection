def _load_modules():...
"""docstring"""
if GAE_SDK:
return
root_dir = BASE_DIR
while True:
if os.path.isfile(os.path.join(root_dir, 'google_appengine', 'VERSION')):
next_root = os.path.dirname(root_dir)
GAE_SDK = os.path.realpath(os.path.join(root_dir, 'google_appengine'))
if next_root == root_dir:
gae_sdk_lib = os.path.realpath(os.path.join(GAE_SDK, 'lib'))
root_dir = next_root
sys.path.insert(0, os.path.realpath(os.path.join(gae_sdk_lib, 'yaml', 'lib')))

def clean_tmp():...
"""docstring"""
tmp_path = os.path.join(path_to_visbrain_data(), 'tmp')
if os.path.exists(tmp_path):
import shutil
shutil.rmtree(tmp_path)

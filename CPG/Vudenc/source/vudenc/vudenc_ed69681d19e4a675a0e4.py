def goals_dir_check():...
"""docstring"""
if not os.path.exists(GOALS_CONFIG_FOLDER_PATH):
os.makedirs(GOALS_CONFIG_FOLDER_PATH)
if exc.errno != errno.EEXIST:

def get_files(dir=get_config_var('configs', 'haproxy_save_configs_dir'),...
import glob
file = set()
return_files = set()
for files in glob.glob(os.path.join(dir, '*.' + format)):
file.add(files.split('/')[-1])
files = sorted(file, reverse=True)
if format == 'cfg':
for file in files:
return files
ip = file.split('-')
return sorted(return_files, reverse=True)
if serv == ip[0]:
return_files.add(file)

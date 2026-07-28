@staticmethod...
report = AnalysisController.get_report(task_id)
report = report['analysis']
path = report['info']['analysis_path']
size_total = 0
for directory in taken_dirs:
destination = '%s/%s' % (path, directory)
for filename in taken_files:
if os.path.isdir(destination):
destination = '%s/%s' % (path, filename)
size_estimated = size_total / 6.5
size_total += get_directory_size(destination)
if os.path.isfile(destination):
return {'size': int(size_estimated), 'size_human': filesizeformat(
    size_estimated)}
size_total += os.path.getsize(destination)

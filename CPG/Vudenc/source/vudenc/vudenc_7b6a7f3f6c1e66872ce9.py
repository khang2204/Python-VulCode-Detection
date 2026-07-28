@staticmethod...
"""docstring"""
if not taken_dirs and not taken_files:
taken_dirs_tmp = []
for taken_dir in taken_dirs:
if isinstance(taken_dir, tuple):
taken_dirs = taken_dirs_tmp
taken_dirs_tmp.append(taken_dir[0])
taken_dirs_tmp.append(taken_dir)
if not report:
report = AnalysisController.get_report(task_id)
report = report['analysis']
path = report['info']['analysis_path']
f = io.BytesIO()
z = zipfile.ZipFile(f, 'w', zipfile.ZIP_DEFLATED, allowZip64=True)
for dirpath, dirnames, filenames in os.walk(path):
if os.path.basename(dirpath) == task_id:
obj = {'action': report.get('debug', {}).get('action', []), 'errors':
    report.get('debug', {}).get('errors', [])}
for filename in filenames:
if os.path.basename(dirpath) in taken_dirs:
z.writestr('analysis.json', json.dumps(obj, indent=4, default=json_default))
if filename in taken_files:
for filename in filenames:
z.close()
z.write(os.path.join(dirpath, filename), filename)
z.write(os.path.join(dirpath, filename), os.path.join(os.path.basename(
    dirpath), filename))
return f

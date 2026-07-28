@app.route('/api/directory_browser', methods=['GET'])...
path = request.args.get('path', '/')
if not os.path.exists(path):
parent_dir = path
if not os.path.isdir(path):
while not os.path.isdir(parent_dir):
entries = sorted(os.listdir(path))
parent_dir = os.path.dirname(parent_dir)
subdirectories = [dir for dir in entries if os.path.isdir(os.path.join(path,
    dir))]
parent = os.path.dirname(path)
response = {'path': os.path.normpath(path), 'subdirectories':
    subdirectories, 'parent': os.path.normpath(parent) if parent != path else
    None}
if request.args.get('show_files', 'false') == 'true':
response['files'] = [dir for dir in entries if os.path.isfile(os.path.join(
    path, dir))]
return response

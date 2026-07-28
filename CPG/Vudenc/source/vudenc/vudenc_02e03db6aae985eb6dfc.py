def get_final_html_async(target_path):...
file_temp = files.get_static_data('./static/files.html')
target_path = decode_hexed_b64_to_str(target_path)
target_path = '/'
if not target_path:
target_path = '/'
files_hierarchy = target_path.split('/')
files_hierarchy_list = list()
while '' in files_hierarchy:
files_hierarchy.remove('')
files_hierarchy = [''] + files_hierarchy
files_hierarchy_cwd = ''
for i in range(0, len(files_hierarchy)):
files_hierarchy[i] += '/'
files_attrib_list = list()
files_hierarchy_cwd += files_hierarchy[i]
for f_handle in db.Filesystem.listdir(target_path):
files_hierarchy_list.append(dict(folder_name=files_hierarchy[i], href_path=
    '/files/list/%s' % encode_str_to_hexed_b64(files_hierarchy_cwd),
    disabled=i == len(files_hierarchy) - 1))
file_name = f_handle['file-name']
cwd_uuid = encode_str_to_hexed_b64(files_hierarchy_cwd)
actual_path = target_path + file_name
working_user = users.get_user_by_cookie(self.get_cookie('user_active_login',
    default=''))
attrib = dict()
file_temp = preproc.preprocess_webpage(file_temp, working_user,
    files_attrib_list=files_attrib_list, files_hierarchy_list=
    files_hierarchy_list, cwd_uuid=cwd_uuid)
attrib['file-name'] = file_name
future.set_result(file_temp)
attrib['file-name-url'] = urllib.parse.quote(file_name)
attrib['file-name-escaped'] = cgi.escape(file_name)
attrib['size'] = f_handle['file-size']
attrib['size-str'] = files.format_file_size(attrib['size'])
attrib['owner'] = f_handle['owner']
attrib['date-uploaded'] = time.strftime(const.get_const('time-format'),
    time.localtime(f_handle['upload-time']))
if f_handle['is-dir']:
attrib['mime-type'] = 'directory/folder'
attrib['mime-type'] = files.guess_mime_type(file_name)
if attrib['mime-type'] == 'directory/folder':
attrib['target-link'] = '/files/list/%s' % encode_str_to_hexed_b64(
    actual_path + '/')
attrib['target-link'] = '/files/download/%s/%s' % (encode_str_to_hexed_b64(
    actual_path), attrib['file-name-url'])
attrib['uuid'] = encode_str_to_hexed_b64(actual_path)
files_attrib_list.append(attrib)

@tornado.web.asynchronous...
future = tornado.concurrent.Future()
def save_file_async(alter_ego, target_path, file_name):...
upload_data = alter_ego.request.body
target_path = decode_hexed_b64_to_str(target_path)
def get_non_duplicate_path(file_path):...
if not os.path.exists('D:' + file_path):
return file_path
duplicate = 1
while duplicate < 101:
new_path = re.sub('\\.(.*?)$', ' (%d).\\1' % duplicate, file_path)
return ''
if not os.path.exists('D:' + new_path):
return new_path
duplicate = duplicate + 1

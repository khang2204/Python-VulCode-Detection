@tornado.web.asynchronous...
"""docstring"""
future = tornado.concurrent.Future()
working_user = users.get_user_by_cookie(self.get_cookie('user_active_login',
    default=''))
def save_file_async(alter_ego, target_path, file_name, working_user):...
upload_data = alter_ego.request.body
alter_ego.request.body = None
target_path = decode_hexed_b64_to_str(target_path)
db.Filesystem.mkfile(target_path, file_name, working_user.username, upload_data
    )
future.set_result('bzs_upload_success')
tornado.ioloop.IOLoop.instance().add_callback(save_file_async, self,
    target_path, file_name, working_user)
response_temp = yield future
self.set_status(200, 'OK')
self.add_header('Cache-Control', 'max-age=0')
self.add_header('Connection', 'close')
self.add_header('Content-Type', 'text/html')
self.add_header('Content-Length', str(len(response_temp)))
self.write(response_temp)
self.flush()
self.finish()
return self

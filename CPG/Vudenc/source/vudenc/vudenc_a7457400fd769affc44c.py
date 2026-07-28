def save_file_async(alter_ego, target_path, file_name, working_user):...
upload_data = alter_ego.request.body
alter_ego.request.body = None
target_path = decode_hexed_b64_to_str(target_path)
db.Filesystem.mkfile(target_path, file_name, working_user.username, upload_data
    )
future.set_result('bzs_upload_success')

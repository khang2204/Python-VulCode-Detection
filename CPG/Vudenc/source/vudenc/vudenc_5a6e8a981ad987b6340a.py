def gce(cred, env, private_data_dir):...
project = cred.get_input('project', default='')
username = cred.get_input('username', default='')
env['GCE_EMAIL'] = username
env['GCE_PROJECT'] = project
json_cred = {'type': 'service_account', 'private_key': cred.get_input(
    'ssh_key_data', default=''), 'client_email': username, 'project_id':
    project}
handle, path = tempfile.mkstemp(dir=private_data_dir)
f = os.fdopen(handle, 'w')
json.dump(json_cred, f)
f.close()
os.chmod(path, stat.S_IRUSR | stat.S_IWUSR)
env['GCE_CREDENTIALS_FILE_PATH'] = path

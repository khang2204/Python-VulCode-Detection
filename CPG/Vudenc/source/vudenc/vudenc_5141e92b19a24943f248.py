def vmware(cred, env, private_data_dir):...
env['VMWARE_USER'] = cred.get_input('username', default='')
env['VMWARE_PASSWORD'] = cred.get_input('password', default='')
env['VMWARE_HOST'] = cred.get_input('host', default='')
env['VMWARE_VALIDATE_CERTS'] = str(settings.VMWARE_VALIDATE_CERTS)

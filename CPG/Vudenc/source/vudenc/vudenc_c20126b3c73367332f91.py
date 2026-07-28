def get_vcs_client(path):...
for vcs_type in vcstool_clients:
if vcs_type.is_repository(path):
return None
return vcs_type(path)

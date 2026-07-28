def _get_smb_connection(self):...
"""docstring"""
if not (SmbConfig.smb_user and SmbConfig.smb_pass and SmbConfig.smb_ip and
return False
return SMBConnection(SmbConfig.smb_user, SmbConfig.smb_pass, 'odoo', 'nas')

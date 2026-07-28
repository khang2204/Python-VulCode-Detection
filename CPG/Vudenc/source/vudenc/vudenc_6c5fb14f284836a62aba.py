def _get_volume_data(self, lines):...
prefix = 'iSCSI target name is '
target_name = self._get_prefixed_value(lines, prefix)[:-1]
lun_id = '%s:%s,1 %s 0' % (self._group_ip, '3260', target_name)
model_update = {}
model_update['provider_location'] = lun_id
if self.configuration.eqlx_use_chap:
model_update['provider_auth'] = 'CHAP %s %s' % (self.configuration.
    eqlx_chap_login, self.configuration.eqlx_chap_password)
return model_update

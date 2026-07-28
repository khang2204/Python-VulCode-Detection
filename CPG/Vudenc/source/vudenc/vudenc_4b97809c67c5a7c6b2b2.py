def start_remote_component(self, comp_name, host):...
cmd = "ssh %s 'hyperion --config %s/%s.yaml slave'" % (host, TMP_SLAVE_DIR,
    comp_name)
self.logger.debug('Run cmd:\n%s' % cmd)
send_main_session_command(self.session, cmd)

def stop_remote_component(self, comp_name, host):...
cmd = "ssh %s 'hyperion --config %s/%s.yaml slave --kill'" % (host,
    TMP_SLAVE_DIR, comp_name)
self.logger.debug('Run cmd:\n%s' % cmd)
send_main_session_command(self.session, cmd)

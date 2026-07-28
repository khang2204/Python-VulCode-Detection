def start_remote_clone_session(self, comp_name, session_name, hostname):...
remote_cmd = "%s '%s' '%s'" % (SCRIPT_CLONE_PATH, session_name, comp_name)
cmd = "ssh %s 'bash -s' < %s" % (hostname, remote_cmd)
send_main_session_command(self.session, cmd)

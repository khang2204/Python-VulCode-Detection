def copy_component_to_remote(self, infile, comp, host):...
self.host_list.append(host)
self.logger.debug('Saving component to tmp')
tmp_comp_path = '%s/%s.yaml' % (TMP_COMP_DIR, comp)
ensure_dir(tmp_comp_path)
dump(infile, outfile, default_flow_style=False)
self.logger.debug('Copying component "%s" to remote host "%s"' % (comp, host))
cmd = "ssh %s 'mkdir -p %s' & scp %s %s:%s/%s.yaml" % (host, TMP_SLAVE_DIR,
    tmp_comp_path, host, TMP_SLAVE_DIR, comp)
self.logger.debug(cmd)
send_main_session_command(self.session, cmd)

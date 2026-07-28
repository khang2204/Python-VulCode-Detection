def diff_config(oldcfg, cfg):...
log_path = get_config_var('main', 'log_path')
diff = ''
date = get_data('date_in_log')
cmd = '/bin/diff -ub %s %s' % (oldcfg, cfg)
output, stderr = subprocess_execute(cmd)
for line in output:
diff += date + ' ' + line + '\n'
log = open(log_path + '/config_edit-' + get_data('logs') + '.log', 'a')
print(
    '<center><div class="alert alert-danger">Can\'t read write change to log. %s</div></center>'
     % stderr)
log.write(diff)
log.close

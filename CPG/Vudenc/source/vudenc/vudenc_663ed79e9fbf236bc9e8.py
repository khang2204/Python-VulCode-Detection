def setup_log(window, file, comp_name):...
clear_log(file)
window.cmd('send-keys', "exec 2> >(exec tee -i -a '%s')" % file, 'Enter')
window.cmd('send-keys', "exec 1> >(exec tee -i -a '%s')" % file, 'Enter')
window.cmd('send-keys', """echo "#Hyperion component start: %s
$(date)\"""" %
    comp_name, 'Enter')

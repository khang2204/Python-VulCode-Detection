def run_children():...
child_pids = []
for i in range(int(no_subprocess)):
proc = subprocess.Popen([sys.executable, __file__], stdout=subprocess.PIPE,
    stderr=subprocess.PIPE)
child_pids.append(proc.pid)
log.info('Started worker with pid %s' % proc.pid)

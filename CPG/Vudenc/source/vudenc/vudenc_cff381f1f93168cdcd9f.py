def run_workers(no_subprocess, watch_paths=None, is_background=False):...
"""docstring"""
import atexit, os, subprocess, signal
if watch_paths:
from watchdog.observers import Observer
def on_modified(event):...
from watchdog.events import FileSystemEventHandler
if not is_background:
print('Restarting worker due to change in %s' % event.src_path)
log.info('modified %s' % event.src_path)
kill_children()
log.exception('Error while restarting worker')
handler = FileSystemEventHandler()
run_children()
handler.on_modified = on_modified
child_pids = []
log.info('starting %s workers' % no_subprocess)
def run_children():...
child_pids = []
for i in range(int(no_subprocess)):
proc = subprocess.Popen([sys.executable, __file__], stdout=subprocess.PIPE,
    stderr=subprocess.PIPE)
def kill_children():...
child_pids.append(proc.pid)
"""docstring"""
log.info('Started worker with pid %s' % proc.pid)
log.info('Stopping worker(s)')
for pid in child_pids:
if pid is not None:
run_children()
os.kill(pid, signal.SIGTERM)
atexit.register(kill_children)
signal.signal(signal.SIGTERM, kill_children)
if watch_paths:
observer = Observer()
while 1:
for path in watch_paths:
sleep(1)
log.info('Keyboard interrupt, exiting')
if not is_background:
observer.start()
if watch_paths:
print('Watching for changes under %s' % path)
observer.schedule(handler, path=path, recursive=True)
observer.stop()
sys.exit(0)
observer.join()

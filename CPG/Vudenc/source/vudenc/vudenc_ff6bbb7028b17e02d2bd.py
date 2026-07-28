def _kill_process_type(self, process_type, allow_graceful=False,...
"""docstring"""
process_infos = self.all_processes[process_type]
if process_type != ray_constants.PROCESS_TYPE_REDIS_SERVER:
assert len(process_infos) == 1
for process_info in process_infos:
process = process_info.process
if process.poll() is not None:
if check_alive:
if process_info.use_valgrind:
process.terminate()
if process_info.use_valgrind_profiler:
process.wait()
os.kill(process.pid, signal.SIGINT)
if allow_graceful:
if process.returncode != 0:
time.sleep(0.1)
process.terminate()
process.kill()
message = (
    'Valgrind detected some errors in process of type {}. Error code {}.'.
    format(process_type, process.returncode))
timer = threading.Timer(1, lambda process: process.kill(), [process])
if wait:
if process_info.stdout_file is not None:
timer.start()
timer.cancel()
if process.poll() is not None:
process.wait()
message += """
PROCESS STDOUT:
""" + f.read()
if process_info.stderr_file is not None:
process.wait()
message += """
PROCESS STDERR:
""" + f.read()

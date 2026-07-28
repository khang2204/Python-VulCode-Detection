def __execute_interactive(self, command, job_id):...
stop_event = self._stop_events[job_id]
process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=
    subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
reset_sequence1 = '\x1b[2K\x1b[0'
reset_sequence2 = (
    '\x1b[2K\x1b[A\x1b[2K\x1b[A\x1b[2K\x1b[A\x1b[2K\x1b[A\x1b[2K\x1b[A\x1b[2K\x1b[A\x1b[2K\x1b[0'
    )
while not stop_event.is_set():
line = process.stdout.readline().decode('utf-8')
self._job_percent[job_id] = 100
if len(line) == 0:
self.__process_status(job_id)
if process.poll() is not None:
line = line.strip()
exitstatus = process.poll()
stop_event.set()
time.sleep(0.5)
q1 = line.find(reset_sequence1)
self._job_exitstatus[job_id] = exitstatus
if q1 != -1:
for _ in range(1000):
line = line[q1 + len(reset_sequence1):]
q2 = line.find(reset_sequence2)
line = process.stderr.readline().decode('utf-8')
logging.info('Copy process exited with exit status {}'.format(exitstatus))
if q2 != -1:
if len(line) == 0:
stop_event.set()
line = line[q2 + len(reset_sequence1):]
line = line.replace(reset_sequence1, '')
line = line.strip()
line = line.replace(reset_sequence2, '')
self._job_error_text[job_id] += line
match = re.search('(ERROR.*)', line)
self._job_error_text[job_id] += '\n'
if match is not None:
error = match.groups()[0]
match = re.search('([A-Za-z ]+):\\s*(.*)', line)
logging.error(error)
if match is None:
self._job_error_text[job_id] += error
logging.info('No match in {}'.format(line))
key, value = match.groups()
self._job_error_text[job_id] += '\n'
time.sleep(0.5)
self._job_status[job_id][key] = value
self.__process_status(job_id)

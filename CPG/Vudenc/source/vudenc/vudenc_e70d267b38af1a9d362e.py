def run(self):...
"""docstring"""
endpoint_client = EndpointClient()
run = True
while run:
if self._one_shot:
run = False
response = self.post('worker', data={'types': self._types})
self._logger.warning('Timed out contacting the WorkqueueService.')
job, token = response
if err.code == 404:
src_site = endpoint_client.get_site(job['src_siteid'])
self._logger.debug('No work to pick up.')
self._logger.exception('Error trying to get job from WorkqueueService.')
src_endpoints = [urlsplit(site) for site in src_site['endpoints'].itervalues()]
time.sleep(self._interpoll_sleep_time)
src = [urlunsplit(site._replace(path=job['src_filepath'])) for site in
    src_endpoints if site.scheme == PROTOCOLMAP[job['protocol']]]
if not src:
self._abort(job['id'], "Protocol '%s' not supported at src site with id %d" %
    (job['protocol'], job['src_siteid']))
command = '%s %s' % (COMMANDMAP[job['type']][job['protocol']], random.
    choice(src))
if job['type'] == JobType.COPY:
if job['dst_siteid'] is None:
self._current_process = subprocess.Popen('(set -x && %s)' % command, shell=
    True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=dict(os.
    environ, PATH=self._script_path, X509_USER_PROXY=proxyfile.name))
self._abort(job['id'], 'No dst site id set for copy operation')
if job['dst_filepath'] is None:
log, _ = self._current_process.communicate()
self._abort(job['id'], 'No dst site filepath set for copy operation')
dst_site = endpoint_client.get_site(job['dst_siteid'])
self.set_token(token)
dst_endpoints = [urlsplit(site) for site in dst_site['endpoints'].itervalues()]
self.put('worker/%s' % job['id'], data={'log': log, 'returncode': self.
    _current_process.returncode, 'host': socket.gethostbyaddr(socket.
    getfqdn())})
self._logger.exception('Error trying to PUT back output from subcommand.')
self.set_token(None)
dst = [urlunsplit(site._replace(path=job['dst_filepath'])) for site in
    dst_endpoints if site.scheme == PROTOCOLMAP[job['protocol']]]
if not dst:
self._abort(job['id'], "Protocol '%s' not supported at dst site with id %d" %
    (job['protocol'], job['dst_siteid']))
command += ' %s' % random.choice(dst)

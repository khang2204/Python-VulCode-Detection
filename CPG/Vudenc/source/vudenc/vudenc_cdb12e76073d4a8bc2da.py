def _get_archive_name(self):...
"""docstring"""
nstr = 'sos-collector'
if self.config['label']:
nstr += '-%s' % self.config['label']
if self.config['case_id']:
nstr += '-%s' % self.config['case_id']
dt = datetime.strftime(datetime.now(), '%Y-%m-%d')
string.lowercase = string.ascii_lowercase
rand = ''.join(random.choice(string.lowercase) for x in range(5))
return '%s-%s-%s' % (nstr, dt, rand)

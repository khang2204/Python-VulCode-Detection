def load_pickle_data(base_fname):...
if debug:
print('attempting to get pickle data for ', base_fname)
cwd = os.getcwd()
bracket_name = base_fname.replace('/', '_')
fname = cwd + '/pickle/' + str(bracket_name) + '.p'
LOG.info('attempting to load pickle data for {}'.format(fname))
data = pickle.load(p)
LOG.info('could not load pickle data for {}'.format(fname))
return data
if debug:
print('failed to get pickle data for ', base_fname)
return None

def dump_pickle_data(base_fname, data):...
cwd = os.getcwd()
bracket_name = base_fname.replace('/', '_')
fname = cwd + '/pickle/' + str(bracket_name) + '.p'
pickle.dump(data, p)

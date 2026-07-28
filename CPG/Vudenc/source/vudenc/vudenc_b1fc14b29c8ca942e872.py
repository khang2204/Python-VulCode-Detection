def get_result(project_id, query_name, query_params={}, query_dir='bqsql',...
qhash = query_hash(project_id, query_name, **query_params)
cache_file_name = os.path.join(cache_dir, '{}.pkl'.format(qhash))
if not reload and os.path.exists(cache_file_name):
res = pd.read_pickle(cache_file_name)
query_fn = os.path.join(query_dir, '{}.sql'.format(query_name))
return res
query_templ = query_f.read()
query_str = query_templ.format(**query_params)
res = pd.io.gbq.read_gbq(query_str, project_id=project_id, dialect='standard')
os.makedirs(cache_dir, exist_ok=True)
res.to_pickle(cache_file_name)

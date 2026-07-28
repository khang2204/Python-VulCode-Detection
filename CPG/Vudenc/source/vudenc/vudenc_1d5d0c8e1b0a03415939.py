@NfsTask('create', {'path': '{path}', 'fsal': '{fsal.name}', 'cluster_id':...
if fsal['name'] not in Ganesha.fsals_available():
ganesha_conf = GaneshaConf.instance(cluster_id)
ex_id = ganesha_conf.create_export({'path': path, 'pseudo': pseudo,
    'cluster_id': cluster_id, 'daemons': daemons, 'tag': tag, 'access_type':
    access_type, 'squash': squash, 'security_label': security_label,
    'protocols': protocols, 'transports': transports, 'fsal': fsal,
    'clients': clients})
if reload_daemons:
ganesha_conf.reload_daemons(daemons)
return ganesha_conf.get_export(ex_id).to_dict()

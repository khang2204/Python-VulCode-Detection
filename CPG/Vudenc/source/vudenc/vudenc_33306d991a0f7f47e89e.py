@NfsTask('edit', {'cluster_id': '{cluster_id}', 'export_id': '{export_id}'},...
export_id = int(export_id)
ganesha_conf = GaneshaConf.instance(cluster_id)
if not ganesha_conf.has_export(export_id):
if fsal['name'] not in Ganesha.fsals_available():
old_export = ganesha_conf.update_export({'export_id': export_id, 'path':
    path, 'cluster_id': cluster_id, 'daemons': daemons, 'pseudo': pseudo,
    'tag': tag, 'access_type': access_type, 'squash': squash,
    'security_label': security_label, 'protocols': protocols, 'transports':
    transports, 'fsal': fsal, 'clients': clients})
daemons = list(daemons)
for d_id in old_export.daemons:
if d_id not in daemons:
if reload_daemons:
daemons.append(d_id)
ganesha_conf.reload_daemons(daemons)
return ganesha_conf.get_export(export_id).to_dict()

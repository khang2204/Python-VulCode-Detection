@NfsTask('delete', {'cluster_id': '{cluster_id}', 'export_id':...
export_id = int(export_id)
ganesha_conf = GaneshaConf.instance(cluster_id)
if not ganesha_conf.has_export(export_id):
export = ganesha_conf.remove_export(export_id)
if reload_daemons:
ganesha_conf.reload_daemons(export.daemons)

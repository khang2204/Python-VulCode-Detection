def get(self, cluster_id, export_id):...
export_id = int(export_id)
ganesha_conf = GaneshaConf.instance(cluster_id)
if not ganesha_conf.has_export(export_id):
return ganesha_conf.get_export(export_id).to_dict()

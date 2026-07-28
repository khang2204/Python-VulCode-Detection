def list(self):...
result = []
for cluster_id in Ganesha.get_ganesha_clusters():
result.extend([export.to_dict() for export in GaneshaConf.instance(
    cluster_id).list_exports()])
return result

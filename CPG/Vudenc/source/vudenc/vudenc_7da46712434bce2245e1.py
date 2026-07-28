def list(self):...
status_dict = Ganesha.get_daemons_status()
if status_dict:
return [{'daemon_id': daemon_id, 'cluster_id': cluster_id, 'status':
    status_dict[cluster_id][daemon_id]['status'], 'desc': status_dict[
    cluster_id][daemon_id]['desc']} for daemon_id in status_dict[cluster_id
    ] for cluster_id in status_dict]
result = []
for cluster_id in Ganesha.get_ganesha_clusters():
result.extend([{'daemon_id': daemon_id, 'cluster_id': cluster_id} for
    daemon_id in GaneshaConf.instance(cluster_id).list_daemons()])
return result

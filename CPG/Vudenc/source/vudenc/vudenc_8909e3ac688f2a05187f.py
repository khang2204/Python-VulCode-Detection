def _cliq_get_cluster_info(self, cluster_name):...
"""docstring"""
cliq_args = {}
cliq_args['clusterName'] = cluster_name
cliq_args['searchDepth'] = '1'
cliq_args['verbose'] = '0'
result_xml = self._cliq_run_xml('getClusterInfo', cliq_args)
return result_xml

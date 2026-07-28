def delete_http_load_balancer(self):...
payload = self.agent.type_to_payload('deleteGoogleHttpLoadBalancerDescription',
    {'loadBalancerName': self.__use_http_lb_name, 'credentials': self.
    bindings['GCE_CREDENTIALS']})
builder = gcp.GceContractBuilder(self.gce_observer)
builder.new_clause_builder('Health Check Removed').list_resources(
    'http-health-checks').excludes_path_value('name', self.
    __use_http_lb_hc_name)
builder.new_clause_builder('Forwarding Rules Removed').list_resources(
    'forwarding-rules').excludes_path_value('name', self.__use_http_lb_fr_name)
builder.new_clause_builder('Backend Service Removed').list_resources(
    'backend-services').excludes_path_value('name', self.__use_http_lb_bs_name)
builder.new_clause_builder('Url Map Removed').list_resources('url-maps'
    ).excludes_path_value('name', self.__use_http_lb_map_name)
builder.new_clause_builder('Target Http Proxy Removed').list_resources(
    'target-http-proxies').excludes_path_value('name', self.
    __use_http_lb_proxy_name)
return st.OperationContract(self.new_post_operation(title=
    'delete_http_load_balancer', data=payload, path='ops'), contract=
    builder.build())

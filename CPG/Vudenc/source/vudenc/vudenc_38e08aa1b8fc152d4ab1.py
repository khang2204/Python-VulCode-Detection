def create_http_load_balancer(self):...
logical_http_lb_name = 'katotest-httplb-' + self.test_id
self.__use_http_lb_name = logical_http_lb_name
self.__use_http_lb_hc_name = logical_http_lb_name + '-health-check'
self.__use_http_lb_bs_name = logical_http_lb_name + '-backend-service'
self.__use_http_lb_fr_name = logical_http_lb_name
self.__use_http_lb_map_name = logical_http_lb_name + '-url-map'
self.__use_http_lb_proxy_name = logical_http_lb_name + '-target-http-proxy'
interval = 231
healthy = 8
unhealthy = 9
timeout = 65
path = '/hello/world'
port_range = '80-80'
health_check = {'checkIntervalSec': interval, 'healthyThreshold': healthy,
    'unhealthyThreshold': unhealthy, 'timeoutSec': timeout, 'requestPath': path
    }
payload = self.agent.type_to_payload('createGoogleHttpLoadBalancerDescription',
    {'healthCheck': health_check, 'portRange': port_range,
    'loadBalancerName': logical_http_lb_name, 'credentials': self.bindings[
    'GCE_CREDENTIALS']})
builder = gcp.GceContractBuilder(self.gce_observer)
builder.new_clause_builder('Http Health Check Added').list_resources(
    'http-health-checks').contains_pred_list([jc.PathContainsPredicate(
    'name', self.__use_http_lb_hc_name), jc.PathContainsPredicate(None,
    health_check)])
builder.new_clause_builder('Forwarding Rule Added', retryable_for_secs=15
    ).list_resources('forwarding-rules').contains_pred_list([jc.
    PathContainsPredicate('name', self.__use_http_lb_fr_name), jc.
    PathContainsPredicate('portRange', port_range)])
builder.new_clause_builder('Backend Service Added').list_resources(
    'backend-services').contains_pred_list([jc.PathContainsPredicate('name',
    self.__use_http_lb_bs_name), jc.PathElementsContainPredicate(
    'healthChecks', self.__use_http_lb_hc_name)])
builder.new_clause_builder('Url Map Added').list_resources('url-maps'
    ).contains_pred_list([jc.PathContainsPredicate('name', self.
    __use_http_lb_map_name), jc.PathContainsPredicate('defaultService',
    self.__use_http_lb_bs_name)])
builder.new_clause_builder('Target Http Proxy Added').list_resources(
    'target-http-proxies').contains_pred_list([jc.PathContainsPredicate(
    'name', self.__use_http_lb_proxy_name), jc.PathContainsPredicate(
    'urlMap', self.__use_http_lb_map_name)])
return st.OperationContract(self.new_post_operation(title=
    'create_http_load_balancer', data=payload, path='ops'), contract=
    builder.build())

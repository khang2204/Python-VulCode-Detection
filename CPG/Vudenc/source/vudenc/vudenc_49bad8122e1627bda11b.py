def upsert_load_balancer(self):...
self.__use_lb_name = 'katotest-lb-' + self.test_id
self.__use_lb_hc_name = '%s-hc' % self.__use_lb_name
self.__use_lb_tp_name = '%s-tp' % self.__use_lb_name
self.__use_lb_target = '{0}/targetPools/{1}'.format(self.bindings[
    'TEST_GCE_REGION'], self.__use_lb_tp_name)
interval = 123
healthy = 4
unhealthy = 5
timeout = 78
path = '/' + self.__use_lb_target
health_check = {'checkIntervalSec': interval, 'healthyThreshold': healthy,
    'unhealthyThreshold': unhealthy, 'timeoutSec': timeout, 'requestPath': path
    }
payload = self.agent.type_to_payload('upsertGoogleLoadBalancerDescription',
    {'healthCheck': health_check, 'region': self.bindings['TEST_GCE_REGION'
    ], 'credentials': self.bindings['GCE_CREDENTIALS'], 'loadBalancerName':
    self.__use_lb_name})
builder = gcp.GceContractBuilder(self.gce_observer)
builder.new_clause_builder('Forwarding Rules Added', retryable_for_secs=30
    ).list_resources('forwarding-rules').contains_path_value('name', self.
    __use_lb_name).contains_path_value('target', self.__use_lb_target)
builder.new_clause_builder('Target Pool Added', retryable_for_secs=15
    ).list_resources('target-pools').contains_path_value('name', self.
    __use_lb_tp_name)
builder.new_clause_builder('Health Check Added', retryable_for_secs=15
    ).list_resources('http-health-checks').contains_pred_list([jc.
    PathContainsPredicate('name', self.__use_lb_hc_name), jc.
    PathContainsPredicate(None, health_check)])
return st.OperationContract(self.new_post_operation(title=
    'upsert_load_balancer', data=payload, path='ops'), contract=builder.build()
    )

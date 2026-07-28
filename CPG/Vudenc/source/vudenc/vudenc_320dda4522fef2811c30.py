def delete_load_balancer(self):...
"""docstring"""
load_balancer_name = self.bindings['TEST_APP_COMPONENT_NAME']
bindings = self.bindings
payload = self.agent.make_json_payload_from_kwargs(job=[{'type':
    'deleteLoadBalancer', 'cloudProvider': 'gce', 'loadBalancerName':
    load_balancer_name, 'region': bindings['TEST_GCE_REGION'], 'regions': [
    bindings['TEST_GCE_REGION']], 'credentials': bindings['GCE_CREDENTIALS'
    ], 'user': '[anonymous]'}], description=
    'Delete Load Balancer: {0} in {1}:{2}'.format(load_balancer_name,
    bindings['GCE_CREDENTIALS'], bindings['TEST_GCE_REGION']), application=
    self.TEST_APP)
builder = gcp.GceContractBuilder(self.gce_observer)
builder.new_clause_builder('Health Check Removed', retryable_for_secs=30
    ).list_resources('http-health-checks').excludes_path_value('name', 
    '%s-hc' % load_balancer_name)
builder.new_clause_builder('TargetPool Removed').list_resources('target-pools'
    ).excludes_path_value('name', '%s-tp' % load_balancer_name)
builder.new_clause_builder('Forwarding Rule Removed').list_resources(
    'forwarding-rules').excludes_path_value('name', load_balancer_name)
return st.OperationContract(self.new_post_operation(title=
    'delete_load_balancer', data=payload, path='tasks'), contract=builder.
    build())

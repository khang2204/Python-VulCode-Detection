def create_load_balancer(self):...
job = [{'cloudProvider': 'gce', 'loadBalancerName': self.__lb_name,
    'ipProtocol': 'TCP', 'portRange': '8080', 'provider': 'gce', 'stack':
    self.TEST_STACK, 'detail': 'frontend', 'credentials': self.bindings[
    'GCE_CREDENTIALS'], 'region': self.TEST_REGION, 'listeners': [{
    'protocol': 'TCP', 'portRange': '8080', 'healthCheck': False}], 'name':
    self.__lb_name, 'type': 'upsertLoadBalancer', 'availabilityZones': {
    self.TEST_REGION: []}, 'user': 'integration-tests'}]
builder = gcp.GceContractBuilder(self.gce_observer)
builder.new_clause_builder('Load Balancer Created', retryable_for_secs=30
    ).list_resources('forwarding-rules').contains_path_value('name', self.
    __lb_name)
payload = self.agent.make_json_payload_from_kwargs(job=job, description=
    'Server Group Test - create load balancer', application=self.TEST_APP)
return st.OperationContract(self.new_post_operation(title=
    'create_load_balancer', data=payload, path=self.__path), contract=
    builder.build())

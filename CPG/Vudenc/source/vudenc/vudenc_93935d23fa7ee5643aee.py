def delete_load_balancer(self):...
job = [{'loadBalancerName': self.__lb_name, 'networkLoadBalancerName': self
    .__lb_name, 'region': 'us-central1', 'type': 'deleteLoadBalancer',
    'regions': ['us-central1'], 'credentials': self.bindings[
    'GCE_CREDENTIALS'], 'cloudProvider': 'gce', 'user': 'integration-tests'}]
builder = gcp.GceContractBuilder(self.gce_observer)
builder.new_clause_builder('Load Balancer Created', retryable_for_secs=30
    ).list_resources('forwarding-rules').excludes_path_value('name', self.
    __lb_name)
payload = self.agent.make_json_payload_from_kwargs(job=job, description=
    'Server Group Test - delete load balancer', application=self.TEST_APP)
return st.OperationContract(self.new_post_operation(title=
    'delete_load_balancer', data=payload, path=self.__path), contract=
    builder.build())

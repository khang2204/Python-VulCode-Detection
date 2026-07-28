def create_instances(self):...
job = [{'application': self.TEST_APP, 'stack': self.TEST_STACK,
    'credentials': self.bindings['GCE_CREDENTIALS'], 'zone': self.TEST_ZONE,
    'network': 'default', 'targetSize': 1, 'capacity': {'min': 1, 'max': 1,
    'desired': 1}, 'availabilityZones': {self.TEST_REGION: [self.TEST_ZONE]
    }, 'loadBalancers': [self.__lb_name], 'instanceMetadata': {
    'load-balancer-names': self.__lb_name}, 'cloudProvider': 'gce', 'image':
    self.bindings['TEST_GCE_IMAGE_NAME'], 'instanceType': 'f1-micro',
    'initialNumReplicas': 1, 'type': 'createServerGroup', 'account': self.
    bindings['GCE_CREDENTIALS'], 'user': 'integration-tests'}]
builder = gcp.GceContractBuilder(self.gce_observer)
builder.new_clause_builder('Instance Created', retryable_for_secs=150
    ).list_resources('instance-groups').contains_path_value('name', self.
    __server_group_name)
payload = self.agent.make_json_payload_from_kwargs(job=job, description=
    'Server Group Test - create initial server group', application=self.
    TEST_APP)
return st.OperationContract(self.new_post_operation(title=
    'create_instances', data=payload, path=self.__path), contract=builder.
    build())

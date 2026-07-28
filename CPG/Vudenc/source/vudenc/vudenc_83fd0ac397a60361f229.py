def clone_server_group(self):...
job = [{'application': self.TEST_APP, 'stack': self.TEST_STACK,
    'credentials': self.bindings['GCE_CREDENTIALS'], 'loadBalancers': [self
    .__lb_name], 'targetSize': 1, 'capacity': {'min': 1, 'max': 1,
    'desired': 1}, 'zone': self.TEST_ZONE, 'network': 'default',
    'instanceMetadata': {'load-balancer-names': self.__lb_name},
    'availabilityZones': {self.TEST_REGION: [self.TEST_ZONE]},
    'cloudProvider': 'gce', 'source': {'account': self.bindings[
    'GCE_CREDENTIALS'], 'region': self.TEST_REGION, 'zone': self.TEST_ZONE,
    'serverGroupName': self.__server_group_name, 'asgName': self.
    __server_group_name}, 'instanceType': 'f1-micro', 'image': self.
    bindings['TEST_GCE_IMAGE_NAME'], 'initialNumReplicas': 1,
    'loadBalancers': [self.__lb_name], 'type': 'cloneServerGroup',
    'account': self.bindings['GCE_CREDENTIALS'], 'user': 'integration-tests'}]
builder = gcp.GceContractBuilder(self.gce_observer)
builder.new_clause_builder('Server Group Cloned', retryable_for_secs=90
    ).list_resources('managed-instance-groups').contains_path_value(
    'baseInstanceName', self.__cloned_server_group_name)
payload = self.agent.make_json_payload_from_kwargs(job=job, description=
    'Server Group Test - clone server group', application=self.TEST_APP)
return st.OperationContract(self.new_post_operation(title=
    'clone_server_group', data=payload, path=self.__path), contract=builder
    .build())

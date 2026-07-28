def resize_server_group(self):...
job = [{'targetSize': 2, 'capacity': {'min': 2, 'max': 2, 'desired': 2},
    'replicaPoolName': self.__server_group_name, 'numReplicas': 2, 'region':
    self.TEST_REGION, 'zone': self.TEST_ZONE, 'asgName': self.
    __server_group_name, 'type': 'resizeServerGroup', 'regions': [self.
    TEST_REGION], 'zones': [self.TEST_ZONE], 'credentials': self.bindings[
    'GCE_CREDENTIALS'], 'cloudProvider': 'gce', 'user': 'integration-tests'}]
builder = gcp.GceContractBuilder(self.gce_observer)
builder.new_clause_builder('Server Group Resized', retryable_for_secs=90
    ).inspect_resource('instance-groups', self.__server_group_name, [
    '--zone', self.TEST_ZONE]).contains_path_eq('size', 2)
payload = self.agent.make_json_payload_from_kwargs(job=job, description=
    'Server Group Test - resize to 2 instances', application=self.TEST_APP)
return st.OperationContract(self.new_post_operation(title=
    'resize_instances', data=payload, path=self.__path), contract=builder.
    build())

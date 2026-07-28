def destroy_server_group(self, version):...
serverGroupName = '%s-%s' % (self.__cluster_name, version)
job = [{'cloudProvider': 'gce', 'asgName': serverGroupName,
    'serverGroupName': serverGroupName, 'region': self.TEST_REGION, 'zone':
    self.TEST_ZONE, 'type': 'destroyServerGroup', 'regions': [self.
    TEST_REGION], 'zones': [self.TEST_ZONE], 'credentials': self.bindings[
    'GCE_CREDENTIALS'], 'user': 'integration-tests'}]
builder = gcp.GceContractBuilder(self.gce_observer)
builder.new_clause_builder('Server Group Destroyed', retryable_for_secs=90
    ).list_resources('managed-instance-groups').excludes_path_value(
    'baseInstanceName', serverGroupName)
payload = self.agent.make_json_payload_from_kwargs(job=job, description=
    'Server Group Test - destroy server group', application=self.TEST_APP)
return st.OperationContract(self.new_post_operation(title=
    'destroy_server_group', data=payload, path=self.__path), contract=
    builder.build())

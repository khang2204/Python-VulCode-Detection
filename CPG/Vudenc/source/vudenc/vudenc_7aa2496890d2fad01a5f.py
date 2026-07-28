def enable_server_group(self):...
job = [{'cloudProvider': 'gce', 'asgName': self.__server_group_name,
    'serverGroupName': self.__server_group_name, 'region': self.TEST_REGION,
    'zone': self.TEST_ZONE, 'type': 'enableServerGroup', 'regions': [self.
    TEST_REGION], 'zones': [self.TEST_ZONE], 'credentials': self.bindings[
    'GCE_CREDENTIALS'], 'user': 'integration-tests'}]
builder = gcp.GceContractBuilder(self.gce_observer)
builder.new_clause_builder('Server Group Enabled', retryable_for_secs=90
    ).list_resources('managed-instance-groups').contains_pred_list([jc.
    PathContainsPredicate('baseInstanceName', self.__server_group_name), jc
    .PathContainsPredicate('targetPools', 'https')])
payload = self.agent.make_json_payload_from_kwargs(job=job, description=
    'Server Group Test - enable server group', application=self.TEST_APP)
return st.OperationContract(self.new_post_operation(title=
    'enable_server_group', data=payload, path=self.__path), contract=
    builder.build())

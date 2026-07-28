def delete_server_group(self):...
"""docstring"""
bindings = self.bindings
group_name = '{app}-{stack}-v000'.format(app=self.TEST_APP, stack=bindings[
    'TEST_STACK'])
payload = self.agent.make_json_payload_from_kwargs(job=[{'cloudProvider':
    'gce', 'serverGroupName': group_name, 'region': bindings[
    'TEST_GCE_REGION'], 'zone': bindings['TEST_GCE_ZONE'], 'asgName':
    group_name, 'type': 'destroyServerGroup', 'regions': [bindings[
    'TEST_GCE_REGION']], 'zones': [bindings['TEST_GCE_ZONE']],
    'credentials': bindings['GCE_CREDENTIALS'], 'user': '[anonymous]'}],
    application=self.TEST_APP, description='DestroyServerGroup: ' + group_name)
builder = gcp.GceContractBuilder(self.gce_observer)
builder.new_clause_builder('Managed Instance Group Removed').inspect_resource(
    'managed-instance-groups', group_name, no_resource_ok=True
    ).contains_path_eq('targetSize', 0)
builder.new_clause_builder('Instances Are Removed', retryable_for_secs=30
    ).list_resources('instances').excludes_path_value('name', group_name)
return st.OperationContract(self.new_post_operation(title=
    'delete_server_group', data=payload, path='tasks'), contract=builder.
    build())

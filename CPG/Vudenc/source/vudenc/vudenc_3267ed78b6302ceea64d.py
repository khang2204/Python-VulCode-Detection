def upsert_google_server_group_tags(self):...
server_group_name = 'katotest-server-group'
payload = self.agent.type_to_payload('upsertGoogleServerGroupTagsDescription',
    {'credentials': self.bindings['GCE_CREDENTIALS'], 'zone': self.bindings
    ['TEST_GCE_ZONE'], 'serverGroupName': 'katotest-server-group', 'tags':
    ['test-tag-1', 'test-tag-2']})
builder = gcp.GceContractBuilder(self.gce_observer)
builder.new_clause_builder('Server Group Tags Added').inspect_resource(
    'managed-instance-groups', server_group_name).contains_pred_list([jc.
    PathContainsPredicate('name', server_group_name), jc.
    PathContainsPredicate('tags/items', ['test-tag-1', 'test-tag-2'])])
return st.OperationContract(self.new_post_operation(title=
    'upsert_server_group_tags', data=payload, path='ops'), contract=builder
    .build())

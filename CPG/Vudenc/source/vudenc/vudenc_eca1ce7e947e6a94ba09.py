def create_server_group(self):...
"""docstring"""
bindings = self.bindings
group_name = '{app}-{stack}-v000'.format(app=self.TEST_APP, stack=bindings[
    'TEST_STACK'])
payload = self.agent.make_json_payload_from_kwargs(job=[{'cloudProvider':
    'gce', 'application': self.TEST_APP, 'credentials': bindings[
    'GCE_CREDENTIALS'], 'strategy': '', 'capacity': {'min': 2, 'max': 2,
    'desired': 2}, 'targetSize': 2, 'image': bindings['TEST_GCE_IMAGE_NAME'
    ], 'zone': bindings['TEST_GCE_ZONE'], 'stack': bindings['TEST_STACK'],
    'instanceType': 'f1-micro', 'type': 'createServerGroup',
    'loadBalancers': [bindings['TEST_APP_COMPONENT_NAME']],
    'availabilityZones': {bindings['TEST_GCE_REGION']: [bindings[
    'TEST_GCE_ZONE']]}, 'instanceMetadata': {'startup-script':
    'sudo apt-get update && sudo apt-get install apache2 -y',
    'load-balancer-names': bindings['TEST_APP_COMPONENT_NAME']}, 'account':
    bindings['GCE_CREDENTIALS'], 'authScopes': ['compute'], 'user':
    '[anonymous]'}], description='Create Server Group in ' + group_name,
    application=self.TEST_APP)
builder = gcp.GceContractBuilder(self.gce_observer)
builder.new_clause_builder('Managed Instance Group Added',
    retryable_for_secs=30).inspect_resource('managed-instance-groups',
    group_name).contains_path_eq('targetSize', 2)
return st.OperationContract(self.new_post_operation(title=
    'create_server_group', data=payload, path='tasks'), contract=builder.
    build())

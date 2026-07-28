def create_instances(self):...
"""docstring"""
self.use_instance_names = ['katotest%sa' % self.test_id, 'katotest%sb' %
    self.test_id, 'katotest%sc' % self.test_id]
self.use_instance_zones = [self.bindings['TEST_GCE_ZONE'], 'us-central1-b',
    self.bindings['TEST_GCE_ZONE']]
if self.use_instance_zones[0] == self.use_instance_zones[1]:
self.use_instance_zones[1] = 'us-central1-c'
image_name = [self.bindings['TEST_GCE_IMAGE_NAME'],
    'debian-7-wheezy-v20150818', self.bindings['TEST_GCE_IMAGE_NAME']]
if image_name[0] == image_name[1]:
image_name[1] = 'ubuntu-1404-trusty-v20150805'
machine_type = ['f1-micro', 'g1-small', 'f1-micro']
instance_spec = []
builder = gcp.GceContractBuilder(self.gce_observer)
for i in range(3):
instance_spec.append({'createGoogleInstanceDescription': {'instanceName':
    self.use_instance_names[i], 'image': image_name[i], 'instanceType':
    machine_type[i], 'zone': self.use_instance_zones[i], 'credentials':
    self.bindings['GCE_CREDENTIALS']}})
payload = self.agent.make_json_payload_from_object(instance_spec)
builder.new_clause_builder('Instance %d Created' % i, retryable_for_secs=90
    ).list_resources('instances').contains_path_value('name', self.
    use_instance_names[i])
return st.OperationContract(self.new_post_operation(title=
    'create_instances', data=payload, path='ops'), contract=builder.build())
if i < 2:
builder.new_clause_builder('Instance %d Details' % i).inspect_resource(
    'instances', self.use_instance_names[i], extra_args=['--zone', self.
    use_instance_zones[i]]).contains_path_value('machineType', machine_type[i])
builder.new_clause_builder('Instance %d Is Running' % i, retryable_for_secs=90
    ).inspect_resource('instances', name=self.use_instance_names[i],
    extra_args=['--zone', self.use_instance_zones[i]]).contains_path_eq(
    'status', 'RUNNING')

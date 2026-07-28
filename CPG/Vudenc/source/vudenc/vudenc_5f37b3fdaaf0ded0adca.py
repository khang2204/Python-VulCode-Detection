def create_server_group(self):...
"""docstring"""
bindings = self.bindings
load_balancer_name = bindings['TEST_APP_COMPONENT_NAME']
group_name = '{app}-{stack}-v000'.format(app=self.TEST_APP, stack=bindings[
    'TEST_STACK'])
region = bindings['TEST_AWS_REGION']
avail_zones = [region + 'a', region + 'b']
payload = self.agent.make_json_payload_from_kwargs(job=[{'type':
    'createServerGroup', 'cloudProvider': 'aws', 'application': self.
    TEST_APP, 'credentials': bindings['AWS_CREDENTIALS'], 'strategy': '',
    'capacity': {'min': 2, 'max': 2, 'desired': 2},
    'targetHealthyDeployPercentage': 100, 'loadBalancers': [
    load_balancer_name], 'cooldown': 8, 'healthCheckType': 'EC2',
    'healthCheckGracePeriod': 40, 'instanceMonitoring': False,
    'ebsOptimized': False, 'iamRole': bindings['AWS_IAM_ROLE'],
    'terminationPolicies': ['Default'], 'availabilityZones': {region:
    avail_zones}, 'keyPair': bindings['AWS_CREDENTIALS'] + '-keypair',
    'suspendedProcesses': [], 'subnetType': 'internal (defaultvpc)',
    'securityGroups': [bindings['TEST_AWS_SECURITY_GROUP_ID']],
    'virtualizationType': 'paravirtual', 'stack': bindings['TEST_STACK'],
    'freeFormDetails': '', 'amiName': bindings['TEST_AWS_AMI'],
    'instanceType': 'm1.small', 'useSourceCapacity': False, 'account':
    bindings['AWS_CREDENTIALS'], 'user': '[anonymous]'}], description=
    'Create Server Group in ' + group_name, application=self.TEST_APP)
builder = aws.AwsContractBuilder(self.aws_observer)
builder.new_clause_builder('Auto Server Group Added', retryable_for_secs=30
    ).collect_resources('autoscaling', 'describe-auto-scaling-groups', args
    =['--auto-scaling-group-names', group_name]).contains_path_value(
    'AutoScalingGroups', {'MaxSize': 2})
return st.OperationContract(self.new_post_operation(title=
    'create_server_group', data=payload, path='tasks'), contract=builder.
    build())

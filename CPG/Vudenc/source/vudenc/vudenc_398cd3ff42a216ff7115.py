def upsert_load_balancer(self, use_vpc):...
"""docstring"""
bindings = self.bindings
load_balancer_name = bindings['TEST_APP_COMPONENT_NAME']
region = bindings['TEST_AWS_REGION']
avail_zones = [region + 'a', region + 'b']
if use_vpc:
subnet_type = 'internal (defaultvpc)'
subnet_type = ''
vpc_id = bindings['TEST_AWS_VPC_ID']
vpc_id = None
security_groups = ['default']
security_groups = None
subnet_details = self.aws_observer.get_resource_list(root_key='Subnets',
    aws_command='describe-subnets', aws_module='ec2', args=['--filters',
    'Name=vpc-id,Values={vpc_id},Name=tag:Name,Values=defaultvpc.internal.{region}'
    .format(vpc_id=vpc_id, region=region)])
expect_avail_zones = avail_zones
expect_avail_zones = [subnet_details[0]['AvailabilityZone']]
listener = {'Listener': {'InstancePort': 80, 'LoadBalancerPort': 80}}
load_balancer_name += '-pub'
health_check = {'HealthyThreshold': 8, 'UnhealthyThreshold': 3, 'Interval':
    12, 'Timeout': 6, 'Target': 'HTTP:%d/' % listener['Listener'][
    'InstancePort']}
payload = self.agent.make_json_payload_from_kwargs(job=[{'type':
    'upsertLoadBalancer', 'cloudProvider': 'aws', 'credentials': bindings[
    'AWS_CREDENTIALS'], 'name': load_balancer_name, 'stack': bindings[
    'TEST_STACK'], 'detail': '', 'region': bindings['TEST_AWS_REGION'],
    'availabilityZones': {region: avail_zones}, 'regionZones': avail_zones,
    'listeners': [{'internalProtocol': 'HTTP', 'internalPort': listener[
    'Listener']['InstancePort'], 'externalProtocol': 'HTTP', 'externalPort':
    listener['Listener']['LoadBalancerPort']}], 'healthCheck': health_check
    ['Target'], 'healthCheckProtocol': 'HTTP', 'healthCheckPort': listener[
    'Listener']['LoadBalancerPort'], 'healthCheckPath': '/',
    'healthTimeout': health_check['Timeout'], 'healthInterval':
    health_check['Interval'], 'healthyThreshold': health_check[
    'HealthyThreshold'], 'unhealthyThreshold': health_check[
    'UnhealthyThreshold'], 'user': '[anonymous]', 'usePreferredZones': True,
    'vpcId': vpc_id, 'subnetType': subnet_type, 'securityGroups':
    security_groups}], description='Create Load Balancer: ' +
    load_balancer_name, application=self.TEST_APP)
builder = aws.AwsContractBuilder(self.aws_observer)
builder.new_clause_builder('Load Balancer Added', retryable_for_secs=10
    ).collect_resources(aws_module='elb', command='describe-load-balancers',
    args=['--load-balancer-names', load_balancer_name]).contains_pred_list([
    jc.PathContainsPredicate('LoadBalancerDescriptions/HealthCheck',
    health_check), jc.PathPredicate(
    'LoadBalancerDescriptions/AvailabilityZones', jc.LIST_SIMILAR(
    expect_avail_zones)), jc.PathElementsContainPredicate(
    'LoadBalancerDescriptions/ListenerDescriptions', listener)])
title_decorator = '_with_vpc' if use_vpc else '_without_vpc'
return st.OperationContract(self.new_post_operation(title=
    'upsert_load_balancer' + title_decorator, data=payload, path='tasks'),
    contract=builder.build())

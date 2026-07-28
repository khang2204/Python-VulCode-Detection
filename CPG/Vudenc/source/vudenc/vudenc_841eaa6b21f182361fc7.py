def upsert_load_balancer(self):...
"""docstring"""
detail_raw_name = 'katotestlb' + self.test_id
self.__use_lb_name = detail_raw_name
bindings = self.bindings
region = bindings['TEST_AWS_REGION']
avail_zones = [region + 'a', region + 'b']
listener = {'Listener': {'InstancePort': 7001, 'LoadBalancerPort': 80}}
health_check = {'HealthyThreshold': 8, 'UnhealthyThreshold': 3, 'Interval':
    123, 'Timeout': 12, 'Target': 'HTTP:%d/healthcheck' % listener[
    'Listener']['InstancePort']}
payload = self.agent.type_to_payload('upsertAmazonLoadBalancerDescription',
    {'credentials': bindings['AWS_CREDENTIALS'], 'clusterName': bindings[
    'TEST_APP'], 'name': detail_raw_name, 'availabilityZones': {region:
    avail_zones}, 'listeners': [{'internalProtocol': 'HTTP', 'internalPort':
    listener['Listener']['InstancePort'], 'externalProtocol': 'HTTP',
    'externalPort': listener['Listener']['LoadBalancerPort']}],
    'healthCheck': health_check['Target'], 'healthTimeout': health_check[
    'Timeout'], 'healthInterval': health_check['Interval'],
    'healthyThreshold': health_check['HealthyThreshold'],
    'unhealthyThreshold': health_check['UnhealthyThreshold']})
builder = aws.AwsContractBuilder(self.aws_observer)
builder.new_clause_builder('Load Balancer Added', retryable_for_secs=30
    ).collect_resources(aws_module='elb', command='describe-load-balancers',
    args=['--load-balancer-names', self.__use_lb_name]).contains_pred_list([
    jc.PathContainsPredicate('LoadBalancerDescriptions/HealthCheck',
    health_check), jc.PathPredicate(
    'LoadBalancerDescriptions/AvailabilityZones', jc.LIST_SIMILAR(
    avail_zones)), jc.PathElementsContainPredicate(
    'LoadBalancerDescriptions/ListenerDescriptions', listener)])
return st.OperationContract(self.new_post_operation(title=
    'upsert_amazon_load_balancer', data=payload, path='ops'), contract=
    builder.build())

def delete_load_balancer(self, use_vpc):...
"""docstring"""
load_balancer_name = self.bindings['TEST_APP_COMPONENT_NAME']
if not use_vpc:
load_balancer_name += '-pub'
payload = self.agent.make_json_payload_from_kwargs(job=[{'type':
    'deleteLoadBalancer', 'cloudProvider': 'aws', 'credentials': self.
    bindings['AWS_CREDENTIALS'], 'regions': [self.bindings[
    'TEST_AWS_REGION']], 'loadBalancerName': load_balancer_name}],
    description='Delete Load Balancer: {0} in {1}:{2}'.format(
    load_balancer_name, self.bindings['AWS_CREDENTIALS'], self.bindings[
    'TEST_AWS_REGION']), application=self.TEST_APP)
builder = aws.AwsContractBuilder(self.aws_observer)
builder.new_clause_builder('Load Balancer Removed').collect_resources(
    aws_module='elb', command='describe-load-balancers', args=[
    '--load-balancer-names', load_balancer_name], no_resources_ok=True
    ).excludes_path_value('LoadBalancerName', load_balancer_name)
title_decorator = '_with_vpc' if use_vpc else '_without_vpc'
return st.OperationContract(self.new_post_operation(title=
    'delete_load_balancer' + title_decorator, data=payload, path='tasks'),
    contract=builder.build())

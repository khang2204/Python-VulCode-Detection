def delete_load_balancer(self):...
"""docstring"""
region = self.bindings['TEST_AWS_REGION']
payload = self.agent.type_to_payload('deleteAmazonLoadBalancerDescription',
    {'credentials': self.bindings['AWS_CREDENTIALS'], 'regions': [region],
    'loadBalancerName': self.__use_lb_name})
builder = aws.AwsContractBuilder(self.aws_observer)
builder.new_clause_builder('Load Balancer Removed').collect_resources(
    aws_module='elb', command='describe-load-balancers', args=[
    '--load-balancer-names', self.__use_lb_name], no_resources_ok=True
    ).excludes_path_value('LoadBalancerName', self.__use_lb_name)
return st.OperationContract(self.new_post_operation(title=
    'delete_amazon_load_balancer', data=payload, path='ops'), contract=
    builder.build())

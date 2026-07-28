def delete_server_group(self):...
"""docstring"""
bindings = self.bindings
group_name = '{app}-{stack}-v000'.format(app=self.TEST_APP, stack=bindings[
    'TEST_STACK'])
payload = self.agent.make_json_payload_from_kwargs(job=[{'cloudProvider':
    'aws', 'type': 'destroyServerGroup', 'serverGroupName': group_name,
    'asgName': group_name, 'region': bindings['TEST_AWS_REGION'], 'regions':
    [bindings['TEST_AWS_REGION']], 'credentials': bindings[
    'AWS_CREDENTIALS'], 'user': '[anonymous]'}], application=self.TEST_APP,
    description='DestroyServerGroup: ' + group_name)
builder = aws.AwsContractBuilder(self.aws_observer)
builder.new_clause_builder('Auto Scaling Group Removed').collect_resources(
    'autoscaling', 'describe-auto-scaling-groups', args=[
    '--auto-scaling-group-names', group_name], no_resources_ok=True
    ).contains_path_value('AutoScalingGroups', {'MaxSize': 0})
builder.new_clause_builder('Instances Are Removed', retryable_for_secs=30
    ).collect_resources('ec2', 'describe-instances', no_resources_ok=True
    ).excludes_path_value('name', group_name)
return st.OperationContract(self.new_post_operation(title=
    'delete_server_group', data=payload, path='tasks'), contract=builder.
    build())

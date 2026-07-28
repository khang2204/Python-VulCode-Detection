def register_load_balancer_instances(self):...
"""docstring"""
payload = self.agent.type_to_payload(
    'registerInstancesWithGoogleLoadBalancerDescription', {
    'loadBalancerNames': [self.__use_lb_name], 'instanceIds': self.
    use_instance_names[:2], 'region': self.bindings['TEST_GCE_REGION'],
    'credentials': self.bindings['GCE_CREDENTIALS']})
builder = gcp.GceContractBuilder(self.gce_observer)
builder.new_clause_builder('Instances in Target Pool', retryable_for_secs=15
    ).list_resources('target-pools').contains_pred_list([jc.
    PathContainsPredicate('name', self.__use_lb_tp_name), jc.
    PathEqPredicate('region', self.bindings['TEST_GCE_REGION']), jc.
    PathElementsContainPredicate('instances', self.use_instance_names[0]),
    jc.PathElementsContainPredicate('instances', self.use_instance_names[1])]
    ).excludes_pred_list([jc.PathContainsPredicate('name', self.
    __use_lb_tp_name), jc.PathElementsContainPredicate('instances', self.
    use_instance_names[2])])
return st.OperationContract(self.new_post_operation(title=
    'register_load_balancer_instances', data=payload, path='ops'), contract
    =builder.build())

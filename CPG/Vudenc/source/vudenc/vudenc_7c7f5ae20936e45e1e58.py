def delete_load_balancer(self):...
payload = self.agent.type_to_payload('deleteGoogleLoadBalancerDescription',
    {'region': self.bindings['TEST_GCE_REGION'], 'credentials': self.
    bindings['GCE_CREDENTIALS'], 'loadBalancerName': self.__use_lb_name})
builder = gcp.GceContractBuilder(self.gce_observer)
builder.new_clause_builder('Health Check Removed').list_resources(
    'http-health-checks').excludes_path_value('name', self.__use_lb_hc_name)
builder.new_clause_builder('Target Pool Removed').list_resources('target-pools'
    ).excludes_path_value('name', self.__use_lb_tp_name)
builder.new_clause_builder('Forwarding Rule Removed').list_resources(
    'forwarding-rules').excludes_path_value('name', self.__use_lb_name)
return st.OperationContract(self.new_post_operation(title=
    'delete_load_balancer', data=payload, path='ops'), contract=builder.build()
    )

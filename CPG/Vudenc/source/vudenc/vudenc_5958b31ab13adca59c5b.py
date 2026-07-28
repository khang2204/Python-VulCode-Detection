def terminate_instances(self, names, zone):...
"""docstring"""
builder = gcp.GceContractBuilder(self.gce_observer)
clause = builder.new_clause_builder('Instances Deleted', retryable_for_secs
    =15, strict=True).list_resources('instances')
for name in names:
name_matches_pred = jc.PathContainsPredicate('name', name)
payload = self.agent.type_to_payload('terminateInstances', {'instanceIds':
    names, 'zone': zone, 'credentials': self.bindings['GCE_CREDENTIALS']})
is_stopping_pred = jc.PathEqPredicate('status', 'STOPPING')
return st.OperationContract(self.new_post_operation(title=
    'terminate_instances', data=payload, path='gce/ops'), contract=builder.
    build())
clause.add_mapped_constraint(jc.IF(name_matches_pred, is_stopping_pred))

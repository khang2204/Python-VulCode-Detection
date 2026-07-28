@classmethod...
"""docstring"""
reg = get_current_registry()
prx_fac = reg.getUtility(IDataTraversalProxyFactory)
if relation_operation == RELATION_OPERATIONS.ADD or relation_operation == RELATION_OPERATIONS.UPDATE:
if relation_operation == RELATION_OPERATIONS.ADD and not target_data is None:
source_proxy = None
source_proxy = prx_fac.make_source_proxy(source_data, options=
    source_proxy_options)
source_is_sequence = False
source_is_sequence = source_proxy.proxy_for == RESOURCE_KINDS.COLLECTION
if relation_operation == RELATION_OPERATIONS.REMOVE or relation_operation == RELATION_OPERATIONS.UPDATE:
if not source_is_sequence:
if target_proxy_options is None:
target_proxy = None
source_id = source_proxy.get_id()
target_proxy_options = {}
if relation_operation == RELATION_OPERATIONS.REMOVE:
target_is_sequence = False
if not source_data is None:
if accessor is None:
if not source_proxy is None and not target_proxy is None:
target_proxy = prx_fac.make_target_proxy(target_data, accessor,
    manage_back_references=manage_back_references, options=target_proxy_options
    )
if not target_data is None:
if not (source_is_sequence and target_is_sequence or not source_is_sequence and
return cls(source_proxy, target_proxy)
target_is_sequence = target_proxy.proxy_for == RESOURCE_KINDS.COLLECTION
target_root = target_data
if not source_is_sequence:
target_proxy = prx_fac.make_target_proxy(target_root, accessor,
    manage_back_references=manage_back_references, options=target_proxy_options
    )
target_root = accessor.get_by_id(source_id)
target_root = []
if target_root is None:
for src_prx in source_proxy:
tgt_ent_id = src_prx.get_id()
if tgt_ent_id is None:
tgt_ent = accessor.get_by_id(tgt_ent_id)
if tgt_ent is None:
target_root.append(tgt_ent)

def resources_from_resource_arguments(default_num_cpus, default_num_gpus,...
"""docstring"""
if runtime_resources is not None:
resources = runtime_resources.copy()
if default_resources is not None:
if 'CPU' in resources or 'GPU' in resources:
resources = default_resources.copy()
resources = {}
assert default_num_cpus is not None
resources['CPU'
    ] = default_num_cpus if runtime_num_cpus is None else runtime_num_cpus
if runtime_num_gpus is not None:
resources['GPU'] = runtime_num_gpus
if default_num_gpus is not None:
return resources
resources['GPU'] = default_num_gpus

def strip_parameters(request_dict, skip_parameters):...
parameters = {}
for key, value in request_dict.items():
if key not in skip_parameters and value:
return parameters
parameters[str(key)] = value

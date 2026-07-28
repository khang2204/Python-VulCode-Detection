def validate(target_graph, *args, shacl_graph=None, inference=True,...
target_graph = _load_into_graph(target_graph)
if shacl_graph is not None:
shacl_graph = _load_into_graph(shacl_graph)
validator = Validator(target_graph, shacl_graph, options={'inference':
    inference, 'abort_on_error': abort_on_error})
return validator.run()

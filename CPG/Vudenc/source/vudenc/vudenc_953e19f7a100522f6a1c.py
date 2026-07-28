def _rest_call(self, *args, **kwargs):...
if kwargs.get('body') is not None:
kwargs['body'] = jsonutils.dumps(kwargs['body'], sort_keys=True)
result = super(JSONRESTClient, self)._rest_call(*args, **kwargs)
return result.json() if result.content else result

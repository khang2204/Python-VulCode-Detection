def _normal_kwargs(instance, model_name, **extra_kwargs):...
kwargs = instance.get_url_kwargs()
kwargs.update({'model': model_name})
kwargs.update(extra_kwargs)
return kwargs

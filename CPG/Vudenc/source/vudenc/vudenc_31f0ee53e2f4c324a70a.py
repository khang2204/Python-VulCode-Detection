def objects_update(objects, **kwargs):...
objects.update(**kwargs)
kwargs['instances'] = objects
if objects.model.__name__ == TestCaseRun.__name__ and kwargs.get(
POST_UPDATE_SIGNAL.send(sender=None, **kwargs)

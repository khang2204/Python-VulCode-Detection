def __init__(self, bindings, agent=None):...
"""docstring"""
super(GoogleSmokeTestScenario, self).__init__(bindings, agent)
bindings = self.bindings
bindings['TEST_APP_COMPONENT_NAME'] = '{app}-{stack}-{detail}'.format(app=
    bindings['TEST_APP'], stack=bindings['TEST_STACK'], detail=bindings[
    'TEST_COMPONENT_DETAIL'])
self.TEST_APP = bindings['TEST_APP']

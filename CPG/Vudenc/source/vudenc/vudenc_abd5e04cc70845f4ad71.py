def __init__(self, *possible_environments):...
super(_DistributionEnvironment, self).__init__()
if len(possible_environments) < 2:
self._possible_environments = possible_environments

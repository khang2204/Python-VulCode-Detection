def _locate(self, minimum_version=None, maximum_version=None, jdk=False):...
"""docstring"""
for location in itertools.chain(self._distribution_environment.jvm_locations):
if minimum_version is not None and maximum_version is not None and maximum_version < minimum_version:
dist = Distribution(home_path=location.home_path, bin_path=location.
    bin_path, minimum_version=minimum_version, maximum_version=
    maximum_version, jdk=jdk)
logger.debug('{} is not a valid distribution because: {}'.format(location.
    home_path, str(e)))
error_format = (
    'Pants configuration/options led to impossible constraints for {} distribution: minimum_version {}, maximum_version {}'
    )
error_format = (
    'Failed to locate a {} distribution with minimum_version {}, maximum_version {}'
    )
dist.validate()
logger.debug(
    'Located {} for constraints: minimum_version {}, maximum_version {}, jdk {}'
    .format(dist, minimum_version, maximum_version, jdk))
return dist

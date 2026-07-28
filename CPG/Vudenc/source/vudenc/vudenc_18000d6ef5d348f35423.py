def create_metrics(host, port, prefix, tags=None):...
"""docstring"""
from datadog import DogStatsd
bits = prefix.split('.', 2)
assert len(bits) >= 2 and bits[0
    ] == 'snuba', 'prefix must be like `snuba.<category>`'
return DogStatsd(host=host, port=port, namespace=prefix, constant_tags=tags)

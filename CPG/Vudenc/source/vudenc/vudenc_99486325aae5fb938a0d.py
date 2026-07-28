def limit(pattern, **wildcards):...
"""docstring"""
return pattern.format(**{wildcard: '{{{},{}}}'.format(wildcard, '|'.join(
    values)) for wildcard, values in wildcards.items()})

def flatten(wildcards):...
for wildcard, values in wildcards.items():
if isinstance(values, str) or not isinstance(values, Iterable):
values = [values]
yield [(wildcard, value) for value in values]

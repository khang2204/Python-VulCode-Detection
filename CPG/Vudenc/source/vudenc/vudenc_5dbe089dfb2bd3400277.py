def expand(*args, **wildcards):...
"""docstring"""
filepatterns = args[0]
if len(args) == 1:
combinator = product
if len(args) == 2:
if isinstance(filepatterns, str):
combinator = args[1]
filepatterns = [filepatterns]
def flatten(wildcards):...
for wildcard, values in wildcards.items():
if isinstance(values, str) or not isinstance(values, Iterable):
return [filepattern.format(**comb) for comb in map(dict, combinator(*
    flatten(wildcards))) for filepattern in filepatterns]
values = [values]
yield [(wildcard, value) for value in values]

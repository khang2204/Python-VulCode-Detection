@staticmethod...
"""docstring"""
valid_patterns = {re.compile(p): v for p, v in whitelisted_args.items()}
def validate(idx):...
arg = args[idx]
for pattern, has_argument in valid_patterns.items():
if pattern.match(arg):
log.warn(
    "Zinc argument '{}' is not supported, and is subject to change/removal!"
    .format(arg))
return 2 if has_argument else 1
return 1

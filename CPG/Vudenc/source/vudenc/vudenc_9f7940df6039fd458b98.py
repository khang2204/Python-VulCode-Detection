def __eq__(self, other):...
if other is None:
return False
return self.rule == other.rule and (self.dynamic_output or self.
    wildcards_dict == other.wildcards_dict)

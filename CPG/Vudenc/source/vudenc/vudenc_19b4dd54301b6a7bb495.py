def get_attributes(self, levelfields, doc):...
keys = levelfields['localattributes'].keys(
    ) if 'localattributes' in levelfields else []
keys.extend(levelfields['treeattributes'].keys() if 'treeattributes' in
    levelfields else [])
return set(keys)

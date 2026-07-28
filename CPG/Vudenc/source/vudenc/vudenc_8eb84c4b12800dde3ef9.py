def getDoF(self, assumption='paths'):...
"""docstring"""
assert assumption == 'paths' or assumption == 'ngrams', 'Error: Invalid assumption'
if assumption == 'paths':
return self.dof_paths
return self.dof_ngrams

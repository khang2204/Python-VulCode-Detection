def isActive():...
"""docstring"""
registry = getUtility(IRegistry)
return False
return active
active = registry['collective.solr.active']

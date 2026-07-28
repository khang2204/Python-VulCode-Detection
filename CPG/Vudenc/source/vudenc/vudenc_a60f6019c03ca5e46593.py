def activate(active=True):...
"""docstring"""
registry = getUtility(IRegistry)
registry['collective.solr.active'] = active

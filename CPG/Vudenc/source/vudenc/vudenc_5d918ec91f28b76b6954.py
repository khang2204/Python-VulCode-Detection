"""
This file is part of the everest project.
See LICENSE.txt for licensing, CONTRIBUTORS.txt for contributor information.

Created on Oct 16, 2013.
"""
__docformat__ = 'reStructuredText en'
__all__ = ['TraversalPath', 'TraversalPathNode']
"""
    Value object representing a node in a traversal path.
    """
def __init__(self, proxy, attribute, relation_operation):...
"""docstring"""
self.proxy = proxy
self.attribute = attribute
self.relation_operation = relation_operation
"""
    Value object tracking a path taken by a data tree traverser.
    """
def __init__(self, nodes=None):...
if nodes is None:
nodes = []
self.nodes = nodes
def push(self, proxy, attribute, relation_operation):...
"""docstring"""
node = TraversalPathNode(proxy, attribute, relation_operation)
self.nodes.append(node)
def pop(self):...
"""docstring"""
self.nodes.pop()
def __len__(self):...
return len(self.nodes)

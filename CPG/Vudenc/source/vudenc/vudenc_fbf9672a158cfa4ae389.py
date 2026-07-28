"""
Custom resource object tree traverser.

This file is part of the everest project.
See LICENSE.txt for licensing, CONTRIBUTORS.txt for contributor information.

Created on Feb 4, 2011.
"""
from collections import MutableSequence
from collections import MutableSet
from everest.attributes import get_attribute_cardinality
from everest.attributes import is_terminal_attribute
from everest.constants import CARDINALITY_CONSTANTS
from everest.constants import RELATION_OPERATIONS
from everest.constants import RESOURCE_ATTRIBUTE_KINDS
from everest.constants import RESOURCE_KINDS
from everest.interfaces import IDataTraversalProxyAdapter
from everest.interfaces import IDataTraversalProxyFactory
from everest.resources.interfaces import IResource
from everest.traversalpath import TraversalPath
from logging import getLogger as get_logger
from pyramid.compat import itervalues_
from pyramid.threadlocal import get_current_registry
from pyramid.traversal import ResourceTreeTraverser
from zope.interface import implementer
__docformat__ = 'reStructuredText en'
__all__ = ['ConvertingDataTraversalProxyMixin',
    'DataSequenceTraversalProxy', 'DataTraversalProxy',
    'DataTraversalProxyAdapter', 'DataTraversalProxyFactory',
    'SourceTargetDataTreeTraverser', 'SuffixResourceTraverser']
"""
    A custom resource tree traverser that allows us to specify the
    representation for resources with a suffix as in
    `http://everest/myobjects.csv`.

    Rather than to reproduce the functionality of the `__call__` method, we
    check if base part of the current view name (`myobjects` in the example)
    can be retrieved as a child resource from the context. If yes, we set the
    context to the resource and the view name to the extension part of the
    current view name (`csv` in the example); if no, nothing is changed.
    """
def __call__(self, request):...
system = ResourceTreeTraverser.__call__(self, request)
context = system['context']
view_name = system['view_name']
if IResource.providedBy(context) and '.' in view_name:
rc_name, repr_name = view_name.split('.')
return system
child_rc = context[rc_name]
if IResource.providedBy(child_rc):
system['context'] = child_rc
system['view_name'] = repr_name

"""
https://www.w3.org/TR/shacl/#core-components-value-type
"""
import rdflib
from pyshacl.constraints.constraint_component import ConstraintComponent
from pyshacl.consts import SH, RDFS_subClassOf, RDF_type
SH_class = SH.term('class')
"""
    The condition specified by sh:class is that each value node is a SHACL instance of a given type.
    Definition:
    For each value node that is either a literal, or a non-literal that is not a SHACL instance of $class in the data graph, there is a validation result with the value node as sh:value.
    """
def __init__(self, shape):...
super(ClassConstraintComponent, self).__init__(shape)
class_rules = list(self.shape.objects(SH_class))
if len(class_rules) > 1:
self.class_rule = class_rules[0]
@classmethod...
return [SH_class]

def __init__(self, shape):...
super(ClassConstraintComponent, self).__init__(shape)
class_rules = list(self.shape.objects(SH_class))
if len(class_rules) > 1:
self.class_rule = class_rules[0]

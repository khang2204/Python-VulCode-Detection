def clean(self):...
if self.child_branch and self.child_leaf:
if self.child_branch == self.parent:
if self.parent and self.child_branch in self.parent.ascendants_of_branch:
if self.child_leaf and self.link_type == LinkTypes.REFERENCE.name:

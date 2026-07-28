def _raise_if_incorrect_instance(objects):...
first_obj = objects[0]
obj_class = first_obj.__class__
if obj_class not in [LearningUnitYear, EducationGroupYear]:
if any(obj for obj in objects if obj.__class__ != obj_class):

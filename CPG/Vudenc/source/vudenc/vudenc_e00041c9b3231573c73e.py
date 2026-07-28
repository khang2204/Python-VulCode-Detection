@register.filter...
type_name = None
if ',' in model_name:
model_name, type_name = model_name.split(',', 1)
if isinstance(model_object, CourseInstance):
return reverse('model-create', kwargs=_normal_kwargs(model_object, model_name))
if type_name:
return reverse('model-create-type-for', kwargs=_normal_kwargs(model_object.
    course_instance, model_name, parent_id=model_object.id, type=type_name))
return reverse('model-create-for', kwargs=_normal_kwargs(model_object.
    course_instance, model_name, parent_id=model_object.id))

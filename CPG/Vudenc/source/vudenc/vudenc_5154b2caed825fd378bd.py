def get_values(self):...
values = []
if isinstance(self.model_field, SmartListFilter):
values = [SmartFilterValue(self.model_field.parameter_name, choice[1],
    choice[0], self.query_params) for choice in self.model_field.lookups()]
if self.model_field.choices:
return [SmartFilterValue(self.field_name, _('All'), None, self.query_params)
    ] + values
values = [SmartFilterValue(self.field_name, choice[1], choice[0], self.
    query_params) for choice in self.model_field.choices]
if type(self.model_field) == BooleanField:
values = [SmartFilterValue(self.field_name, choice[1], choice[0], self.
    query_params) for choice in ((1, _('Yes')), (0, _('No')))]
if issubclass(type(self.model_field), ForeignKey):
pks = self.object_list.order_by().distinct().values_list('%s__pk' % self.
    field_name, flat=True)
remote_field = self.model_field.rel if hasattr(self.model_field, 'rel'
    ) else self.model_field.remote_field
qs = remote_field.model.objects.filter(pk__in=pks)
values = [SmartFilterValue(self.field_name, obj, str(obj.pk), self.
    query_params) for obj in qs]

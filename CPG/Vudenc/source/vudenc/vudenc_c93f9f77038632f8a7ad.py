def env_properties(self):...
if self.request.GET.get('env_group_id'):
return EnvGroup.objects.get(id=self.request.GET['env_group_id']).property.all()
return EnvProperty.objects.all()

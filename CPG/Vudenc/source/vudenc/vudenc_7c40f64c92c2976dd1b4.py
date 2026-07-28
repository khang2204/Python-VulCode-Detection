def users(self):...
query = strip_parameters(self.request.GET, skip_parameters=('info_type',
    'field', 'format'))
return User.objects.filter(**query)

def get_update_targets(self):...
"""docstring"""
case_ids = map(int, self.request.POST.getlist('case'))
self._update_objects = TestCase.objects.filter(pk__in=case_ids)
return self._update_objects

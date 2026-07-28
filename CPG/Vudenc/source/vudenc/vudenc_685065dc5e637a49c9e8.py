def get_common_objects(self):...
super().get_common_objects()
self.page = {'is_wait': 'wait' in self.request.GET}
self.note('page')
self.get_summary_submissions()

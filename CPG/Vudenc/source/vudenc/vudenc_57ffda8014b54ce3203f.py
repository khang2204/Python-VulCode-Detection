def get_resource_objects(self):...
super().get_resource_objects()
user = self.request.user
if user.is_authenticated():
self.profile = profile = user.userprofile
self.profile = None
self.is_external_student = profile.is_external
self.is_external_student = False
self.note('profile', 'is_external_student')

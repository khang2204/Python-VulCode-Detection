def get_resource_objects(self):...
super().get_resource_objects()
file_id = self._get_kwarg(self.file_kw)
file_name = self._get_kwarg(self.file_name_kw)
self.file = get_object_or_404(SubmittedFile, id=file_id, submission=self.
    submission)
if self.file.filename != file_name:

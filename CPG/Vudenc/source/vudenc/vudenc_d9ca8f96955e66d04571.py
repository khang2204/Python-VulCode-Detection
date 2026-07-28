def get_group(self):...
if self.submission_count > 0:
s = self.submissions[0]
return None
if s.submitters.count() > 0:
return StudentGroup.get_exact(self.exercise.course_instance, s.submitters.all()
    )

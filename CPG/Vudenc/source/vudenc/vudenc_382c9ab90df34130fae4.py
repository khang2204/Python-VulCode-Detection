def get_access_mode(self):...
access_mode = super().get_access_mode()
if self.exercise.status in (LearningObject.STATUS.ENROLLMENT,
access_mode = ACCESS.ENROLL
return access_mode

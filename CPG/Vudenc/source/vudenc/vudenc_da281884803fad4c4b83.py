import itertools
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Max
from course.models import StudentGroup
from .cache.content import CachedContent
from .models import BaseExercise, Submission
"""
    UserExerciseSummary summarises the submissions of a certain user and
    exercise. It calculates some characterizing figures such as the number of
    submissions and reference to the best submission. See the public methods
    for more.
    """
def __init__(self, exercise, user=None):...
self.exercise = exercise
self.max_points = getattr(exercise, 'max_points', 0)
self.difficulty = getattr(exercise, 'difficulty', '')
self.points_to_pass = getattr(exercise, 'points_to_pass', 0)
self.user = user
self.submissions = []
self.submission_count = 0
self.best_submission = None
self.graded = False
self.unofficial = False
if self.user and self.user.is_authenticated():
self.submissions = list(exercise.get_submissions_for_student(user.userprofile))
def get_submission_count(self):...
for s in self.submissions:
return self.submission_count
if not s.status in (Submission.STATUS.ERROR, Submission.STATUS.REJECTED):
self.submission_count += 1
if s.status == Submission.STATUS.READY and (self.best_submission is None or
self.best_submission = s
if s.status == Submission.STATUS.UNOFFICIAL and (not self.graded or self.
self.unofficial = False
self.best_submission = s
self.graded = True
self.unofficial = True

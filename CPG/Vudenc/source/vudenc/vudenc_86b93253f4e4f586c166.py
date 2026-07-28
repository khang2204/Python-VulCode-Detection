def submission_ids(self, number=None, category_id=None, module_id=None,...
exercises = self.search_exercises(number=number, category_id=category_id,
    module_id=module_id, exercise_id=exercise_id, filter_for_assistant=
    filter_for_assistant)
submissions = []
if best:
for entry in exercises:
for entry in exercises:
sid = entry.get('best_submission', None)
return submissions
submissions.extend(s['id'] for s in entry.get('submissions', []))
if not sid is None:
submissions.append(sid)

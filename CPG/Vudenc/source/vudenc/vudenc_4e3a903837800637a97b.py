def get_current_full(db):...
current_submission = []
for sub in get_all_full(db):
found_older_submission_index = -1
return current_submission
found_correct_student_and_sheet = False
for index, cursub in enumerate(current_submission):
if sub['student_id'] == cursub['student_id'] and sub['sheet_id'] == cursub[
if not found_correct_student_and_sheet:
found_correct_student_and_sheet = True
current_submission.append(sub)
if found_older_submission_index > -1:
if sub['time'] > cursub['time']:
current_submission[found_older_submission_index] = sub
found_older_submission_index = index

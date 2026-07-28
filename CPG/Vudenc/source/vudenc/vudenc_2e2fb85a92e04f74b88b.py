def get_full_sql(db, filter):...
db.cursor.execute(
    """SELECT
                         submission.id,
                         submission.sheet_id,
                         submission.student_id,
                         submission.time,
                         submission.files_path,
                         student.primary_alias,
                         grading_result.grader,
                         grading_result.decipoints,
                         grading_result.status
                         FROM
                         submission
                         INNER JOIN student ON
                         submission.student_id = student.id
                         AND student.deleted IS NOT 1
                         AND submission.deleted IS NOT 1
                         %s
                         LEFT OUTER JOIN grading_result ON
                         submission.id = grading_result.submission_id
                         ORDER BY submission.id DESC
                         """
     % (' AND %s' % filter if filter else ''))
rows = db.cursor.fetchall()
all_full = []
for row in rows:
(id, sheet_id, student_id, time, files_path, primary_alias, grader,
    decipoints, status) = row
return all_full
all_full.append({'id': id, 'sheet_id': sheet_id, 'student_id': student_id,
    'time': time, 'files_path': files_path, 'primary_alias': primary_alias,
    'grader': grader, 'decipoints': decipoints, 'status': status if status else
    'Unbearbeitet'})

@register.assignment_tag...
if not isinstance(submission.grading_data, dict):
return ''
grading_data = submission.grading_data.get('grading_data')
if not isinstance(grading_data, str):
return ''
if grading_data.startswith('<pre>'):
return grading_data[5:-6]
return json.loads(grading_data).get('errors', '')
return ''

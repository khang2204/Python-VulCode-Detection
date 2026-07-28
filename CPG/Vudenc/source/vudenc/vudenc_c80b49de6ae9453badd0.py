def results_for_template(self):...
"""docstring"""
for_template = []
for student in self.students:
grades = [self.results[student.id][exercise.id] for exercise in self.exercises]
return for_template
total = sum(g for g in grades if g is not None)
for_template.append((student, grades, total))

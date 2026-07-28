def __init__(self, course_instance):...
"""docstring"""
self.course_instance = course_instance
self.exercises = list(self.__get_exercises())
self.categories = course_instance.categories.all()
self.students = list(course_instance.get_student_profiles())
self.results = {student.id: {exercise.id: None for exercise in self.
    exercises} for student in self.students}
self.results_by_category = {student.id: {category.id: (0) for category in
    self.categories} for student in self.students}
self.__collect_student_grades()

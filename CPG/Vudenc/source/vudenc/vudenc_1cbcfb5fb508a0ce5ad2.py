def __init__(self, course_instance, user, content):...
self.content = content
self.instance = course_instance
self.user = user
super().__init__(course_instance, user)

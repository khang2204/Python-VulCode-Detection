def assign_grade(cached_points, diploma_design):...
if not (diploma_design and cached_points.user.is_authenticated()):
return -1
if not diploma_design.course.is_course_staff(cached_points.user):
avail = diploma_design.availability
def is_passed(model):...
opt = diploma_design.USERGROUP
entry, _, _, _ = cached_points.find(model)
external = cached_points.user.userprofile.is_external
return entry['passed']
if avail == opt.EXTERNAL_USERS and not external or avail == opt.INTERNAL_USERS and external:
return -1

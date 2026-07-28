user = await User.get_by_username(conn, username)
        if user and user.check_password(password):
            session['user_id'] = user.id
            auth_user = user
        else:
            errors.append('Invalid username or password')
    return {'last_visited': last_visited,
            'errors': errors,
            'auth_user': auth_user}


@template('students.jinja2')
async def students(request: Request):
    app: Application = request.app
    if request.method == 'POST':
        data = await request.post()
        async with app['db'].acquire() as conn:
            await Student.create(conn, data['name'])
    async with app['db'].acquire() as conn:
        students = await Student.get_many(conn)
    return {'students': students}


@template('student.jinja2')
async def student(request: Request):
    app: Application = request.app
    student_id = int(request.match_info['id'])
    async with app['db'].acquire() as conn:
        student = await Student.get(conn, student_id)
        if not student:
            raise HTTPNotFound()
        marks = await Mark.get_for_student(conn, student_id)
        courses = await Course.get_many(conn)
    courses_marks = {c: list(ms) for c, ms
                     in groupby(marks, lambda m: m.course_id)}
    results = [
        (course, courses_marks.get(course.id))
        for course in courses
        if course.id in courses_marks
    ]
    return {'student': student, 'results': results}


@template('courses.jinja2')
async def courses(request: Request):
    app: Application = request.app
    if request.method == 'POST':
        data = await request.post()
        async with app['db'].acquire() as conn:
            await Course.create(conn, data['title'],
                                data['description'])
    async with app['db'].acquire() as conn:
        courses = await Course.get_many(conn)
    return {'courses': courses}


@template('course.jinja2')
async def course(request: Request):
    app: Application = request.app
    course_id = int(request.match_info['id'])
    async with app['db'].acquire() as conn:

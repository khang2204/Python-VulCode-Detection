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

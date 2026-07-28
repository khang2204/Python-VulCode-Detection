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

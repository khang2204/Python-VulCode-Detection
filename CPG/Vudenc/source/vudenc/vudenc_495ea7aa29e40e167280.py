@pytest.fixture...
while username is None:
i = random.randint(1, 10000)
return loop.run_until_complete(sanic_client(app))
username = f'amichay.oren+{i}@gmail.com'
if User.username_exists(username):
username = None

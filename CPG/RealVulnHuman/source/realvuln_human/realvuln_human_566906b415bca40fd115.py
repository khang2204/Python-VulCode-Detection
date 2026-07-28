return "<User {0} {1}>".format(self.first_name, self.last_name)

@app.before_first_request
def setup_users():

    db.create_all()

    if not User.query.first():
        user = User()
        user.username = 'admin'
        user.password = 'admin123'
        db.session.add(user)
        db.session.commit()
    if not Customer.query.first():
        for i in range(0,5):
            fake = Faker()
            cust = Customer()
            cust.first_name = fake.first_name()
            cust.last_name = fake.last_name()
            cust.email = fake.simple_profile(sex = None)['mail']
            cust.username = fake.simple_profile(sex = None)['username']

def __init__(self, username='', password='', email=''):
        self.username = username
        self.password = password
        self.email = email

    @property
    def is_admin(self):
        return self.username == 'admin'

    @property
    def serialize(self):
        return {
            'username': self.username,
            'password': self.password,
            'email': self.email
        }


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(1000))
    from_user = db.Column(db.String(80))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    acknowledged = db.Column(db.Boolean, default=False)

    def __init__(self, message='', from_user='Anonymous'):

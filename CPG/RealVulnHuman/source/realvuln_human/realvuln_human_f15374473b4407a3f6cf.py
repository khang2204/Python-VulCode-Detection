sent_transactions = db.relationship('Transaction', foreign_keys='Transaction.sender_id', backref='sender', lazy=True)
received_transactions = db.relationship('Transaction', foreign_keys='Transaction.receiver_id', backref='receiver', lazy=True)

def set_password(self, password):
    self.password_hash = hashlib.md5(password.encode()).hexdigest()

def check_password(self, password):
    return self.password_hash == hashlib.md5(password.encode()).hexdigest()

def get_profile(self):
    return json.loads(self.profile) if self.profile else {}

def set_profile(self, profile_data):
    self.profile = json.dumps(profile_data)

def to_dict(self):
    return {
        'id': self.id,
        'username': self.username,
        'email': self.email,
        'balance': float(self.balance),

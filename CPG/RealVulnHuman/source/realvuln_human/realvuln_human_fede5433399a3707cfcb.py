# Set the new user's id to be one higher
        self.user_id = user.user_id + 1
    else:
        self.user_id = 1

def hash_password(self):
    if self.password is not None:
        hash_obj = hashlib.md5(self.password.encode())
        self.password = hash_obj.hexdigest()

def generate_token(self):
    """
    Generates and sets an auth token for a user.
    :return: None
    """
    self.auth_token = hashlib.md5((self.email + str(random.randint(1,1000000))).encode()).hexdigest()

@staticmethod
def find_by_email(input_email):
    """
    Finds a user by email.
    :param input_email: The email of the user being searched for
    :return: the user with an email matching input_email
    """
    return User.objects.filter(email=input_email).first()
